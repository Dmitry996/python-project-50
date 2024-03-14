from gendiff import generate_diff
from pathlib import Path


def get_path(file_name):
    p = Path(__file__)
    current_dir = p.absolute().parent
    return current_dir / 'fixtures' / file_name


def test_generate_diff_json():
    input_1 = get_path('file_1_plain.json')
    input_2 = get_path('file_2_plain.json')
    result = get_path('result_plain.txt')
    with open(result) as result:
        assert generate_diff(input_1, input_2) == result.read()


def test_generate_diff_yaml():
    input_1 = get_path('file_1_plain.yaml')
    input_2 = get_path('file_2_plain.yml')
    result = get_path('result_plain.txt')
    with open(result) as result:
        assert generate_diff(input_1, input_2) == result.read()
