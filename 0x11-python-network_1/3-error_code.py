#!/usr/bin/python3

"""This script sends an HTTP GET request to a specified URL and
prints the response body. If the request results in an HTTP error,
the script prints the error code.
"""

from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError

if __name__ == "__main__":

    url = argv[1]

    try:
        with urlopen(url) as res:
            print(f"{res.read().decode('utf-8')}")
    except HTTPError as err:
        print(f"Error code: {err.status}")
