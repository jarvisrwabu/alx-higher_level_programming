#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > (len(mylist) - 1):
        return None
    else:
        for item in my_list:
            return my_list[idx]
