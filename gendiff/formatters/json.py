import json


def make_json(data):
    """
    Returns diff converted to json format
    Args:
        data: List of dictionaries of differences between two datasets
    """
    return json.dumps(data, indent=2, separators=(',', ': '))
