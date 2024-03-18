from .stylish import make_stylish
from .plain import make_plain


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
            return make_plain(data)

    return ValueError('unsupported format')
