#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    lenSize = len(my_list)
    if idx < 0 or idx >= lenSize:
        return my_list
    my_list[idx] = element
    return my_list
