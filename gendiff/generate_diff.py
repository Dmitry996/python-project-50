from .parser import open_file
from .formatters.choice_format import choice_format
from .diff_generator import diff_generator


def generate_diff(path_to_file_1: str, path_to_file_2: str, formatter='stylish'):  # noqa: E501
    """Returns changes to the contents of the second file relative to the first.
    Args:
        first_file: Path to the source file.
        second_file: Path to the modified file."""

    file_1: dict = open_file(path_to_file_1)
    file_2: dict = open_file(path_to_file_2)

    gendiff_paths = f'gendiff {path_to_file_1} {path_to_file_2}'
    print(gendiff_paths)
    diff = diff_generator(file_1, file_2)
    result = choice_format(diff, formatter)
    print(result)
    return result
