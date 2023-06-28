from gendiff.cli import gendiff


def main():
    args = gendiff()
    print(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
