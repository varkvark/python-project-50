import json

import yaml
from yaml.loader import SafeLoader


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


def dict_to_str(new_dict):
    result = '{\n'
    for key, value in new_dict.items():
        new_string = f'{key}: {value}\n'
        result += new_string
    result += '}'
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
            if not isinstance(first_value, dict) or not isinstance(second_value, dict):
                if key in first_dict:
                    result[f'  - {key}'] = first_value
                if key in second_dict:
                    result[f'  + {key}'] = second_value
            else:
                result[f'    {key}'] = compare_dicts(first_value, second_value)

    return sorted_dict(result)


def diff_stylish(new_dict):
    count = 0

    def inner(inner_dict):
        spaces = '    '
        prefix = {'    ', '  + ', '  - '}
        result = '{\n'
        nonlocal count

        for key, value in inner_dict.items():
            if key[:4] in prefix:
                result += f'{spaces * count}{key}: '
            else:
                result += f'{spaces * count}{spaces}{key}: '

            if not isinstance(value, dict):
                result += f'{value}\n'
            else:
                count += 1
                result += f'{inner(value)}\n'
        result += f'{spaces * count}' + '}'
        count -= 1
        return result

    result = inner(new_dict)

    return result


def format_text(text):
    replace = {
        'True': 'true',
        'False': 'false',
        'None': 'null'
    }
    for old, new in replace.items():
        text = text.replace(old, new)
    return text


def generate_diff(first_file, second_file, format_name='stylish'):
    first_dict = open_json_yaml(first_file)
    second_dict = open_json_yaml(second_file)

    result = compare_dicts(first_dict, second_dict)

    if format_name == 'stylish':
        result = diff_stylish(result)
        return format_text(result)
