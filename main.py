# !/usr/bin/env python3
# tree.py

"""This module provides RP Tree entry point script"""

import pathlib
import sys
from rptree.rptree import DirectoryTree
from rptree.cli import CliParser


def read_from_file(filename):
    with open(filename) as f:
        contents = f.read()
    return contents


def main():
    parser = CliParser()
    args = parser.parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified root directory doen't exist")
        sys.exit()
    tree = DirectoryTree(root_dir, dir_only=args.dir_only,
                         output_file=args.output_file)
    tree.generate()
    file_contents = read_from_file(args.output_file)
    print(file_contents)


main()
