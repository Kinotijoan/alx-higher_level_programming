#!/usr/bin/python3
def element_at(my_list, idx):
    lenSize = len(my_list)
    if idx < 0 or idx > lenSize:
        return None
    else:
        for i, v in enumerate(my_list):
            if i == idx:
                return v
