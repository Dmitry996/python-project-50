#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff import get_perser_args


def main():
    first_file, second_file, formatter = get_perser_args()
    result = generate_diff(first_file, second_file, formatter)
    print(result)


if __name__ == '__main__':
    main()
