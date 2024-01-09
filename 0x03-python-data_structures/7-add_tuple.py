#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ''' Extract the first two elements of each tuple,
    using 0 if the tuple is smaller than 2 '''
    a1, a2 = tuple_a[:2] if len(tuple_a) >= 2 else (0, 0)
    b1, b2 = tuple_b[:2] if len(tuple_b) >= 2 else (0, 0)

    # Calculate the sum of the corresponding elements
    sum_first = a1 + b1
    sum_second = a2 + b2

    # Return the result as a tuple
    return (sum_first, sum_second)
