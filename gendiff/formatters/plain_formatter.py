def format_value(value):
    if isinstance(value, dict) or isinstance(value, list):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    else:
        return str(value).lower()


def diff_plain(new_dict):
    dot_path = []
    result = []

    def inner(new_dict):
        nonlocal result
        nonlocal dot_path

        for key in new_dict:
            old = f'  - {key[4:]}'
            new = f'  + {key[4:]}'
            static = f'    {key[4:]}'

            if old in new_dict and new in new_dict:
                dot_path.append(key[4:])
                key_name = ".".join(dot_path)
                dot_path.pop()

                new_line = (
                    f"Property '{key_name}' was updated. "
                    f"From {format_value(new_dict[old])} "
                    f"to {format_value(new_dict[new])}"
                )

                if new_line in result:
                    continue
                result.append(new_line)

            elif old in new_dict and new not in new_dict:
                dot_path.append(key[4:])
                key_name = ".".join(dot_path)
                dot_path.pop()

                new_line = f"Property '{key_name}' was removed"
                result.append(new_line)

            elif old not in new_dict and new in new_dict:
                dot_path.append(key[4:])
                key_name = ".".join(dot_path)
                dot_path.pop()

                new_line = (
                    f"Property '{key_name}' was added "
                    f"with value: {format_value(new_dict[key])}"
                )
                result.append(new_line)

            elif static in new_dict and isinstance(new_dict[static], dict):
                dot_path.append(key[4:])
                inner(new_dict[static])
                dot_path.pop()

    inner(new_dict)

    result = "\n".join(result)

    return result
