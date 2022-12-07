#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    #convert dictionary to list
    dict_list = a_dictionary.items()
    #sorting the list
    dict_list = sorted(dict_list)
    #iterating through the list
    for i in dict_list:
        print(i[0], ":", i[1])
