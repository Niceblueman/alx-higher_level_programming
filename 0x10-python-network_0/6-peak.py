#!/usr/bin/python3
"""Find a peak in unsorted list[int]"""

def find_peak(lst_of_integers):
    """Find a peak in list[int]"""

    if lst_of_integers is None or lst_of_integers == []:
        return None
    low = 0
    high = len(lst_of_integers)
    middle = ((high - low) // 2) + low
    middle = int(middle)
    if high == 1:
        return lst_of_integers[0]
    if high == 2:
        return max(lst_of_integers)
    if lst_of_integers[middle] >= lst_of_integers[middle - 1] and\
            lst_of_integers[middle] >= lst_of_integers[middle + 1]:
        return lst_of_integers[middle]
    if middle > 0 and lst_of_integers[middle] < lst_of_integers[middle + 1]:
        return find_peak(lst_of_integers[middle:])
    if middle > 0 and lst_of_integers[middle] < lst_of_integers[middle - 1]:
        return find_peak(lst_of_integers[:middle])