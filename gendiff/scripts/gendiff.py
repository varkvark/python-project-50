import argparse


def main():
    parser = argparse.ArgumentParser(
        description='''Compares twoconfiguration
        files and shows a difference.'''
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    _ = parser.parse_args()


if __name__ == '__main__':
    main()
