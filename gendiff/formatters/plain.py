def to_string(value):
    """
    Brings the value to the correct string variant.
    Args:
        value: Value
    """
    if isinstance(value, bool):
        return str(value).lower()

    elif isinstance(value, (list, dict)):
        return '[complex value]'

    elif isinstance(value, str):
        return f"'{value}'"

    elif value is None:
        return 'null'
    return value


def make_plain(data: list, path=''):
    """
    Returns a string of differences reduced to plain.
    Args:
        data: List of dictionaries of differences between two datasets
    """
    diff = ''

    def walk(node, path=''):
        node_name = node['name']
        value_old = to_string(node.get("value_old"))
        value_new = to_string(node.get("value_new"))

        match path:
            case '':
                new_path = node_name
            case _:
                new_path = f'{path}.{node_name}'

        match node['status']:
            case 'deleted':
                return f"Property '{new_path}' was removed\n"
            case 'added':
                return (f"Property '{new_path}' was added with "
                        f"value: {value_new}\n")
            case 'modified':
                return (f"Property '{new_path}' was updated. "
                        f"From {value_old} to {value_new}\n")
            case 'node':
                children = node['children']
                return make_plain(children, new_path)

    for node in data:
        formatted_node = walk(node, path)
        if formatted_node is not None:
            diff += formatted_node
    return diff
