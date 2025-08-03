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
