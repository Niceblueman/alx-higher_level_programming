#!/usr/bin/python3
"""Description: This Python script sends an HTTP GET request to a specified URL and
prints the value of the "X-Request-Id" header from the response.

Parameters:
    - URL (str): The URL to send the GET request to.

Usage:
    Run this script by providing the URL as a command-line argument. For example:
    $ python3 script.py https://example.com
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            print(dict(response.headers).get("X-Request-Id"))
    except urllib.error.URLError as e:
        print(f"Error: Unable to retrieve data from the URL: {url}")
        print(f"Reason: {e.reason}")
