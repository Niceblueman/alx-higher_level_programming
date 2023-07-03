#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def mark(s):
        if s is search:
            return replace
        else:
            return s
    return [mark(i) for i in my_list]
