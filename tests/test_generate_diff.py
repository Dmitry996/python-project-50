from gendiff import generate_diff
from pathlib import Path


def get_path(file_name):
    p = Path(__file__)
    current_dir = p.absolute().parent
    return current_dir / 'fixtures' / file_name


def test_generate_diff_json():
    input_1 = get_path('file_1.json')
    input_2 = get_path('file_2.json')
    result = get_path('result.txt')
    with open(result) as result:
        assert generate_diff(input_1, input_2) == result.read()


def test_generate_diff_yaml():
    input_1 = get_path('file_1.yaml')
    input_2 = get_path('file_2.yml')
    result = get_path('result.txt')
    with open(result) as result:
        assert generate_diff(input_1, input_2) == result.read()
