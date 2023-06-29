import argparse
import json
import json


def gendiff():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', "--format", help='set format of output')
    return parser.parse_args()


def generate_diff(first_file, second_file):
    file_1 = json.load(open(first_file))
    file_2 = json.load(open(second_file))
    file_1 = dict(sorted(file_1.items()))
    file_2 = dict(sorted(file_2.items()))
    result = '{\n'
    for key in file_1:
        if key in file_2:
            if file_1[key] == file_2[key]:
                result += f'  {key}: {file_1[key]}\n'
            else:
                result += f'- {key}: {file_1[key]}\n'
                result += f'+ {key}: {file_2[key]}\n'
        else:
            result += f'- {key}: {file_1[key]}\n'
    for key in file_2:
        if key not in file_1:
            result += f'+ {key}: {file_2[key]}\n'
    result += '}'
    return result
