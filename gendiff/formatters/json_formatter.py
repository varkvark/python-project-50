import json


def dict_to_json(new_dict):
    result = {}
    
    for key in new_dict:
        old = f'  - {key[4:]}'
        new = f'  + {key[4:]}'
        static = f'    {key[4:]}'

        if old in new_dict and new in new_dict:
            result[key[4:]] = {
                'status': 'changed',
                'old_value': new_dict[old],
                'new_value': new_dict[new]
            }

            if key[4:] in result:
                continue

        elif old in new_dict and new not in new_dict:
            result[key[4:]] = {
                'status': 'removed',
                'value': new_dict[old]
            }

        elif old not in new_dict and new in new_dict:
            result[key[4:]] = {
                'status': 'added',
                'value': new_dict[new]
            }

        elif static in new_dict:
            if isinstance(new_dict[static], dict):
                result[key[4:]] = dict_to_json(new_dict[static])
            else:
                result[key[4:]] = new_dict[static]

    return result


def diff_json(new_dict):
    result = dict_to_json(new_dict)
    return json.dumps(result, indent="  ")
