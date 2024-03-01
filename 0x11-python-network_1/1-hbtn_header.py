#!/usr/bin/python3

"""This script sends an HTTP GET request to a specified URL and
prints the value of the 'X-Request-Id' header from the response.
"""

from sys import argv
from urllib.request import urlopen

if __name__ == "__main__":

    url_input = argv[1]

    with urlopen(url_input) as res:
        res_headers = res.info()
        print(f'{res_headers["X-Request-Id"]}')
