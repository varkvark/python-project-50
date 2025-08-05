import json

import yaml
from yaml.loader import SafeLoader

from gendiff.formatters.json_formatter import diff_json
from gendiff.formatters.plain_formatter import diff_plain
from gendiff.formatters.stylish_formatter import diff_stylish


def open_json_yaml(filepath):
    if filepath.endswith('.json'):
        with open(filepath) as f:
            return json.load(f)
    elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
        with open(filepath) as f:
            return yaml.load(f, Loader=SafeLoader)


def sorted_dict(new_dict):
    prefix = {'    ', '  + ', '  - '}
    for key in new_dict:
        if key[0:4] in prefix:
            result = dict(
                sorted(new_dict.items(), key=lambda key: key[0][4:])
            )
        else:
            result = dict(
                sorted(new_dict.items(), key=lambda key: key[0])
            )
    return result


def compare_dicts(first_dict, second_dict):
    result = {}

    all_keys = set(first_dict) | set(second_dict)

    for key in all_keys:
        first_value = first_dict.get(key)
        second_value = second_dict.get(key)

        if first_value == second_value:
            result[f'    {key}'] = first_value
        else:
            if not isinstance(first_value, dict) or not isinstance(second_value, dict):  # noqa: E501
                if key in first_dict:
                    result[f'  - {key}'] = first_value
                if key in second_dict:
                    result[f'  + {key}'] = second_value
            else:
                result[f'    {key}'] = compare_dicts(first_value, second_value)

    return sorted_dict(result)


def format_text(string):
    string = (
        string.replace('True', 'true')
        .replace('False', 'false')
        .replace('None', 'null')
    )
    return string


def generate_diff(first_file, second_file, format_name='stylish'):
    first_dict = open_json_yaml(first_file)
    second_dict = open_json_yaml(second_file)

    result = compare_dicts(first_dict, second_dict)

    if format_name == 'stylish':
        result = diff_stylish(result)
    elif format_name == 'plain':
        result = diff_plain(result)
    elif format_name == 'json':
        result = diff_json(result)
    else:
        raise ValueError("Unsupported format")

    return format_text(result)
