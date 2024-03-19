from .parser import get_data
from .formatters import choice_format
from .diff_generator import generate_differences


def generate_diff(path_to_file_1: str, path_to_file_2: str, formatter='stylish'):  # noqa: E501
    """Returns changes to the contents of the second file relative to the first.
    Args:
        first_file: Path to the source file.
        second_file: Path to the modified file."""

    file_1: dict = get_data(path_to_file_1)
    file_2: dict = get_data(path_to_file_2)

    diff = generate_differences(file_1, file_2)
    result = choice_format(diff, formatter)
    return result
