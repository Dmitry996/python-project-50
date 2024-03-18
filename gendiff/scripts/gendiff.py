#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff import parser


def main():
    first_file, second_file, formatter = parser()
    result = generate_diff(first_file, second_file, formatter)
    print(result)


if __name__ == '__main__':
    main()
