#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    [new.update({key: a_dictionary.get(key)*2}) for key in a_dictionary]
    return new
