#!/usr/bin/python3
"""Load arguments, add then save."""
if __name__ == "__main__":
    import sys
    import importlib
    module_one = "5-save_to_json_file"
    module_two = "6-load_from_json_file"

    module_5 = importlib.import_module(module_one)
    module_6 = importlib.import_module(module_two)

    # Get the command line arguments
    arguments = sys.argv[1:]

    try:
        current = module_6.load_from_json_file("add_item.json")

    except FileNotFoundError as e:
        current = []

    # Add new arguments to current list
    current.extend(arguments)

    # Save to JSON
    module_5.save_to_json_file(current, "add_item.json")
