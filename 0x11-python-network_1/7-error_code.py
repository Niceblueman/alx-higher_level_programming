#!/usr/bin/python3
"""solution"""


import sys
import requests

if __name__ == "__main__":
    link = sys.argv[1]

    r = requests.get(link)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
