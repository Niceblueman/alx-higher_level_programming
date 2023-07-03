#!/usr/bin/python3
from dis import dis
def magic_calculation(a, b):
    return a + b ** 98
dis(magic_calculation)