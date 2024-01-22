#!/usr/bin/python3
# Add TypeError
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    return True
