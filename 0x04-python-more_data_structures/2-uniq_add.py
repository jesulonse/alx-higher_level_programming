#!/usr/bin/python3
def uniq_add(my_list=[]):
    #initializing the number as 0
    numb = 0
    for i in set(my_list):
        numb += i
    return numb
