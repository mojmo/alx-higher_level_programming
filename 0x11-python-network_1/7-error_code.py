#!/usr/bin/python3
"""This script sends an HTTP GET request to a specified URL using
the requests library and prints the response body. If the request
results in an HTTP error (status code 400 or higher),
the script prints the error code.
"""

from sys import argv
import requests

if __name__ == "__main__":

    res = requests.get(argv[1])

    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
