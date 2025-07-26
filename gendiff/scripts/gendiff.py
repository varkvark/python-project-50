import argparse

from gendiff.modules import generate_diff


def start_gendiff_cli():
    parser = argparse.ArgumentParser(
        description='''Compares twoconfiguration
        files and shows a difference.'''
    )

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')

    return parser.parse_args()


def main():
    args = start_gendiff_cli()

    first_file = args.first_file
    second_file = args.second_file

    x = generate_diff(first_file, second_file)
    print(x)


if __name__ == '__main__':
    main()
