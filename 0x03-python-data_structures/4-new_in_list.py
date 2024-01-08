#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_to_modify = my_list[:]
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        copy_to_modify[idx] = element
        return copy_to_modify
