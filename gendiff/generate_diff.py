import json


def generate_diff(first_file: str, second_file: str):
    """Returns changes to the contents of the second file relative to the first
    Args:
        first_file: path to the source file
        second_file: path to the modified file """

    file_1: dict = json.load(open(first_file))
    file_2: dict = json.load(open(second_file))

    diff = f'gendiff {first_file} {second_file}\n'
    diff += '{\n'

    for key, value in sorted(file_1.items()):
        if isinstance(value, bool or None):
            value = json.dumps(value)

        if key not in file_2:
            diff += f'  - {key}: {value}\n'

        elif key in file_2 and file_1[key] == file_2[key]:
            diff += f'    {key}: {value}\n'

        elif key in file_2 and file_1[key] != file_2[key]:
            diff += f'  - {key}: {value}\n'
            diff += f'  + {key}: {file_2[key]}\n'

    for key, value in sorted(file_2.items()):
        if isinstance(value, bool or None):
            value = json.dumps(value)

        if key not in file_1:
            diff += f'  + {key}: {value}\n'

    diff += '}\n'
    print(diff)
