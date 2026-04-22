"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True):
        if not isinstance(items, list):
                    raise RuntimeError(f"Cannot sort {type(items)}")

        return sorted(items, reverse=not ascending)


def remove_duplicates_from_list(items):
        return list(set(items))


def create_file(filename, data):
        with open(filename, "w") as f:
                    f.write(data)


def read_file(filename):
        if not os.path.exists(filename):
                    raise FileNotFoundError(f"File {filename} not found")

        with open(filename, "r") as f:
                    return f.read().splitlines()


def main():
        print("Executing main.py")

    if len(sys.argv) < 2:
                filename = DEFAULT_FILENAME
else:
            filename = sys.argv[1]

    if len(sys.argv) < 3:
                duplicates = DEFAULT_DUPLICATES
else:
            duplicates = sys.argv[2].lower() == "true"

    print(f"Reading file: {filename}")
    try:
                items = read_file(filename)
except FileNotFoundError as e:
            print(f"Error: {e}")
            return

    if duplicates:
                print("Removing duplicates")
                items = remove_duplicates_from_list(items)

    print("Sorting list")
    items = sort_list(items)

    print(f"Sorted list: {items}")


if __name__ == "__main__":
        main()
    
