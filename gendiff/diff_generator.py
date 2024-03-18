def for_unchanged(key, value):
    """
    Returns a dictionary for a node that is unchanged.
    Args:
        key: Key
        value: Value
    """
    return {'name': key,
            'status': 'unchanged',
            'value_old': value,
            }


def for_modified(key, value_old, value_new):
    """
    Returns the dictionary for the node that has been modified.
    Args:
        key: Key
        value_old: Value_old
        value_new: Value_new
    """
    return {'name': key,
            'status': 'modified',
            'value_old': value_old,
            'value_new': value_new,
            }


def for_deleted(key, value):
    """
    Returns the dictionary for the node that was deleted.
    Args:
        key: Key
        value: Value
    """
    return {'name': key,
            'status': 'deleted',
            'value_old': value,
            }


def for_added(key, value):
    """
    Returns the dictionary for the node that was added.
    Args:
        key: Key
        value: Value
    """
    return {'name': key,
            'status': 'added',
            'value_new': value,
            }


def for_children(key, value_old, value_new):
    """
    Returns a dictionary for a node that has children
    and applies diff_generator to children.
    Args:
        key: Key
        value_old: Value_old
        value_new: Value_new
    """
    return {'name': key,
            'status': 'node',
            'children': diff_generator(value_old, value_new),
            }


def diff_generator(data_1: dict, data_2: dict):  # noqa: C901
    """
    Generates a dictionary of the difference between two input dictionaries.
    Args:
        data_1: Original dictionary
        data_2: Modified dictionary
    """
    keys = set(data_1.keys() | data_2.keys())
    diff = list()

    for key in keys:
        if key in data_1 and key in data_2:
            value_1 = data_1[key]
            value_2 = data_2[key]

            if isinstance(value_1, dict) and isinstance(value_2, dict):
                diff.append(for_children(key, value_1, value_2))
                continue

            if value_1 == value_2:
                diff.append(for_unchanged(key, data_1[key]))

            if value_1 != value_2:
                diff.append(for_modified(key, value_1, value_2))
        elif key in data_1:
            value = data_1[key]
            diff.append(for_deleted(key, value))

        else:
            value = data_2[key]
            diff.append(for_added(key, value))

    return sorted(diff, key=lambda x: x['name'])
