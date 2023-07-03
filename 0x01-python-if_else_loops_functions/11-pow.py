#!/usr/bin/python3
def pow(a, b):
    return "{:g}".format(a ** b) if b >= 0 else "{:.16g}".format(a ** b)
