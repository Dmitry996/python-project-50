from .stylish import make_stylish
from .plain import make_plain
from .json import make_json


def choice_format(data, format: str):
    """
    Returns a function call corresponding to the formatter
    Args:
        data: Difference between the first and second file
        format: formatter
    """
    match format:
        case 'stylish':
            return make_stylish(data)
        case 'plain':
            return make_plain(data)[:-1]
        case 'json':
            return make_json(data)

    return ValueError('Unsupported format')
