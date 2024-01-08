#!/usr/bin/python3
def no_c(my_string):
    while 'c' in my_string or 'C' in my_string:
        if 'c' in my_string:
            c_index = my_string.find('c')
            my_string = my_string[:c_index] + my_string[c_index + 1:]
        elif 'C' in my_string:
            C_index = my_string.find('C')
            my_string = my_string[:C_index] + my_string[C_index + 1:]
    return my_string
