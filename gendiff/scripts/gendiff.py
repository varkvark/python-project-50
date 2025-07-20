import json
import argparse


def open_json(filepath):
    with open(filepath) as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(
        description='''Compares twoconfiguration
        files and shows a difference.'''
    )

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()

    print(
        open_json(args.first_file),
        open_json(args.second_file),
        sep='\n'
    )


if __name__ == '__main__':
    main()
