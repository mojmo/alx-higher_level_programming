#!/usr/bin/python3
"""
This module updates a JSON file with command line arguments.

Example:
    ./update_json_file.py arg1 arg2 arg3
"""

if __name__ == "__main__":
    import sys
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        li = load_from_json_file("add_item.json")
    except FileNotFoundError:
        li = []

    li += sys.argv[1:]

    save_to_json_file(li, "add_item.json")
