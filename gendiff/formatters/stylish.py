def to_string(value, spaces_count=2):
    """
    Brings the value to the correct string variant.
    Args:
        value: Value
        spaces_count: Number of spaces
    """
    if isinstance(value, bool):
        return str(value).lower()

    elif value is None:
        return 'null'

    elif isinstance(value, dict):
        sep = ' ' * (spaces_count + 4)
        result = ""

        for key, inner_value in value.items():
            format_value = to_string(inner_value, spaces_count + 4)
            result += f"{sep}  {key}: {format_value}\n"

        end_sep = ' ' * (spaces_count + 2)
        return f"{{\n{result}{end_sep}}}"
    return value


def make_stylish(data: list, spaces_count=2):
    """
    Returns a string of differences reduced to stylish.
    Args:
        data: List of dictionaries of differences between two datasets
        spaces_count: Number of spaces
    """

    diff = '{\n'
    sep = ' ' * spaces_count

    for node in data:

        value_old = to_string(node.get("value_old"), spaces_count)
        value_new = to_string(node.get("value_new"), spaces_count)

        match node['status']:
            case 'unchanged':
                diff += f'{sep}  {node["name"]}: {value_old}\n'
            case 'deleted':
                diff += f'{sep}- {node["name"]}: {value_old}\n'
            case 'added':
                diff += f'{sep}+ {node["name"]}: {value_new}\n'
            case 'modified':
                diff += f'{sep}- {node["name"]}: {value_old}\n'
                diff += f'{sep}+ {node["name"]}: {value_new}\n'
            case 'node':
                children = make_stylish(node['children'], spaces_count + 4)
                diff += f'{sep}  {node["name"]}: {children}\n'

    diff += f'{" " * (spaces_count - 2)}}}'
    return diff
