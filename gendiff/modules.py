import json


def open_json(filepath):
    with open(filepath) as f:
        return json.load(f)


def sorted_dict(new_dict):
    result = dict(
        sorted(new_dict.items(), key=lambda key: key[0][4])
    )

    return result


def dict_to_str(new_dict):
    result = '{\n'
    for key, value in new_dict.items():
        new_string = f'{key}: {value}\n'
        result += new_string
    result += '}'
    return result


def generate_diff(first_file, second_file):
    result = {}

    first_json = open_json(first_file)
    second_json = open_json(second_file)

    all_keys = set(first_json) | set(second_json)

    for key in all_keys:
        value_in_first = first_json.get(key)
        value_in_second = second_json.get(key)

        if value_in_first == value_in_second:
            result[f'    {key}'] = value_in_first
        else:
            if key in first_json:
                result[f'  - {key}'] = value_in_first
            if key in second_json:
                result[f'  + {key}'] = value_in_second

    result = sorted_dict(result)

    return dict_to_str(result)
