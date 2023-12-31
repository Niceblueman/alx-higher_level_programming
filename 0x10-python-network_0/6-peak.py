#!/usr/bin/python3
"""Find a peak in unsorted list[int]"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    Args:
        list_of_integers (list): The list of integers.
    Returns:
        int: The peak element if found, otherwise None.
    """
    if not list_of_integers:
        return None
    low = 0
    high = len(list_of_integers) - 1
    while low < high:
        mid = (low + high) // 2
        current = list_of_integers[mid]
        next_element = list_of_integers[mid + 1]
        if current < next_element:
            low = mid + 1
        else:
            high = mid
    return list_of_integers[low]
