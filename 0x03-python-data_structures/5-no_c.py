#!/usr/bin/python3
def no_c(my_string):
    return "".join([x for x in list(my_string) if (x != 'c') and (x != 'C')])
