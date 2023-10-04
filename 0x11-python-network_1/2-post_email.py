#!/usr/bin/python3
"""Description: This Python script sends an HTTP GET request to a specified URL and
prints the value of the "X-Request-Id" header from the response.

Parameters:
    - URL (str): The URL to send the GET request to.

Usage:
    Run this script by providing the URL as a command-line argument. For example:
    $ python3 script.py https://example.com
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    """_summary_
    """
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
