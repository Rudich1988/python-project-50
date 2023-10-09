import argparse

from gendiff import generate_diff
from gendiff.styles.stylish import stylish
from gendiff.styles.plain import plain
from gendiff.styles.json_style.json_style import stylish_12


prog = 'gendiff'
usage = 'usage: gendiff [options] <filepath1> <filepath2>'
description = 'Compares two configuration files and shows a difference.'


def main():
    parser = argparse.ArgumentParser(description, usage)
    parser.add_argument('file_1')
    parser.add_argument('file_2')
    parser.add_argument('-f', '--format', default=stylish,
                        help='output format (default: "stylish")')
    args = parser.parse_args()
    if '--format':
        if args.format == 'plain':
            args.format = plain
        elif args.format == 'json':
            args.format = stylish_12
    print(generate_diff(args.file_1, args.file_2, args.format))


if __name__ == '__main__':
    main()
