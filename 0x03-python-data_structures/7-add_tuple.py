#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """a tuple is smaller than 2, use the value 0 for each""" 
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    """a tuple is bigger than 2, use only the first 2"""
    added_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return added_tuple
