from gendiff.cli import gendiff, generate_diff


def main():
    args = gendiff()
    print(
        generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
