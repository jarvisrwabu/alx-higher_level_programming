#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 1:
        return None
    elif idx > len(mylist):
        return None
    else:
        for item in my_list:
            return my_list[idx]
