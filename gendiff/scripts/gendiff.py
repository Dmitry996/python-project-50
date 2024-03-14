#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff import parser


def main():
    first_file, second_file = parser()
    generate_diff(first_file, second_file)


if __name__ == '__main__':
    main()
