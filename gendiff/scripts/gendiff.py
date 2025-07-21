import argparse
from gendiff.modules import open_json, generate_diff


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
    first_dict = open_json(args.first_file)
    second_dict = open_json(args.second_file)

    x = generate_diff(first_dict, second_dict)
    print(x)


if __name__ == '__main__':
    main()
