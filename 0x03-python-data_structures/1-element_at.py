#!/usr/bin/python3
def element_at(my_list, idx):
    lenSize = len(my_list)
    if i < 0 or i > lenSize:
        return None
    else:
        for i, v in enumerate(my_list):
            if i == idx:
                return v
