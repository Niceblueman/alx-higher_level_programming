#!/usr/bin/python3
for num in range(9):
    for n in range(num+1, 10):
        if (num*10+n) != 89:
            print("{:d}{:d},".format(num, n), end=' ')
        else:
            print("{:d}{:d}".format(num, n))
