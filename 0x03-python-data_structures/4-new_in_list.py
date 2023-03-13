#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lenSize = len(my_list)
    new_list = my_list.copy()
    if idx < 0:
        return my_list
    elif idx > lenSize - 1:
        return new_list
    new_list[idx] = element
    return new_list

