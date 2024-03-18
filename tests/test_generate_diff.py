from gendiff import generate_diff
from pathlib import Path
import pytest


def get_path(file_name):
    p = Path(__file__)
    current_dir = p.absolute().parent
    return current_dir / 'fixtures' / file_name


test_files = [
    ('file_1.json', 'file_2.json', 'result_stylish.txt', 'stylish'),
    ('file_1.yaml', 'file_2.yml', 'result_stylish.txt', 'stylish'),
    ('file_1.yaml', 'file_2.json', 'result_stylish.txt', 'stylish'),
    ('file_1.json', 'file_2.json', 'result_plain.txt', 'plain'),
    ('file_1.yaml', 'file_2.yml', 'result_plain.txt', 'plain'),
    ('file_1.yaml', 'file_2.json', 'result_plain.txt', 'plain')
]


@pytest.mark.parametrize('file_1, file_2, result_file, formatter', test_files)
def test_generate_diff(file_1, file_2, result_file, formatter):
    input_1 = get_path(file_1)
    input_2 = get_path(file_2)
    result = get_path(result_file)
    with open(result) as res:
        assert generate_diff(input_1, input_2, formatter) == res.read()
