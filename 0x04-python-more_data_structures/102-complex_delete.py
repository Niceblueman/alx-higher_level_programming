#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = a_dictionary.copy()
    for k, v in new.items():
        if v is value:
            del new[k]
    return new
