#!/usr/bin/python3
def uniq_add(my_list=[]):
    ulist = []
    [ulist.append(i) for i in my_list if i not in ulist]
    return sum(ulist)
