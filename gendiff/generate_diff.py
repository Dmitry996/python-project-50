import json
from .parser import open_file


def to_sting(value: str):
    if isinstance(value, bool):
        value = str(value).lower()

    if value is None:
        value = 'null'

    return value


def generate_diff(path_to_first_file: str, path_to_second_file: str):
    """Returns changes to the contents of the second file relative to the first
    Args:
        first_file: Path to the source file.
        second_file: Path to the modified file."""

    file_1: dict = open_file(path_to_first_file)
    file_2: dict = open_file(path_to_second_file)

    gendiff_paths = f'gendiff {path_to_first_file} {path_to_second_file}'
    diff = '{\n'

    combined_keys = set(list(file_1.keys()) + list(file_2.keys()))
    for key in sorted(combined_keys):
        if key in file_1 and key in file_2:
            value_1 = to_sting(file_1[key])
            value_2 = to_sting(file_2[key])

            if value_1 == value_2:
                diff += f'    {key}: {value_1}\n'

            else:
                diff += f'  - {key}: {value_1}\n'
                diff += f'  + {key}: {value_2}\n'

        elif key in file_1:
            value_1 = to_sting(file_1[key])
            diff += f'  - {key}: {value_1}\n'

        else:
            value_2 = to_sting(file_2[key])
            diff += f'  + {key}: {value_2}\n'

    diff += '}'
    print(gendiff_paths)
    print(diff)
    return diff
