#!/usr/bin/python3
"""Description: This Python script sends an HTTP GET request to a specific URL
(https://alx-intranet.hbtn.io/status), retrieves the response content, and prints
information about the content.

Parameters:
    This script does not accept any command-line parameters.

Usage:
    Simply run this script, and it will perform an HTTP GET request to the URL
    'https://alx-intranet.hbtn.io/status' and display information about the response.
"""

if __name__ == '__main__':
    import urllib.request

    try:
        with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
            content = res.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
    except urllib.error.URLError as e:
        print(f"Error: Unable to retrieve data from the URL: {url}")
        print(f"Reason: {e.reason}")
