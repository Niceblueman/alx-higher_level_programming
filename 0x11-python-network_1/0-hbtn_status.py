#!/usr/bin/python3
"""Description: This Python script sends an HTTP GET request to a specified URL
and prints information about the response content.

Parameters:
    - URL (str): The URL to send the GET request to.

Usage:
    Run this script by providing the URL as a command-line argument. For example:
    $ python3 script.py https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import urllib.request
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            content = res.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
    except urllib.error.URLError as e:
        print(f"Error: Unable to retrieve data from the URL: {url}")
        print(f"Reason: {e.reason}")
