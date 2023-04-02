#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or No
    """
    size = len(list_of_integers)
    mid_index_elem = size
    mid_index = size // 2

    if size == 0:
        return None

    while True:
        mid_index_elem = mid_index_elem // 2
        #checking the mid element from the top
        if (mid_index < size - 1 and list_of_integers[mid_index] < list_of_integers[mid_index + 1]):
            if mid_index_elem // 2 == 0:
                mid_index_elem = 2
            mid_index = mid_index + mid_index_elem // 2
        #checking the mid element from the bottom
        elif mid_index_elem > 0 and list_of_integers[mid_index] < list_of_integers[mid_index - 1]:
            if mid_index_elem // 2 == 0:
                mid_index_elem = 2
            mid_index = mid_index - mid_index_elem // 2
        else:
            return list_of_integers[mid_index]
