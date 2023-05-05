#!/usr/bin/env python3

import os
import sys
import argparse


def main():
    """
    Entry point of the program. Parses command line arguments and creates the directory structure.
    """
    parser = argparse.ArgumentParser(description='Tool for creating a directory structure for Hack The Box machines')

    # Add an argument for specifying the parent directory name.
    parser.add_argument('-d', dest='parent_dir', required=True, help='specify parent directory name')
    args = parser.parse_args()

    parent_dir = args.parent_dir

    # Check if the parent directory already exists.
    if os.path.exists(parent_dir):
        print("Specified directory already exists!")
        sys.exit()

    # Create the parent directory.
    os.mkdir(parent_dir, mode=0o700)
    print("Directory '%s' is built!" % parent_dir)
    print()

    # Create subdirectories under the parent directory.
    sub_dir_names = ["nmap", "scripts", "notes"]
    for sub_dir_name in sub_dir_names:
        sub_dir = os.path.join(parent_dir, sub_dir_name)
        os.mkdir(sub_dir, mode=0o700)
        print("Directory '%s' is built!" % sub_dir)
        print()


if __name__ == '__main__':
    main()
