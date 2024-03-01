#!/usr/bin/python3

"""This script sends a POST request to a specified URL with an 'email'
parameter and prints the response.
"""

from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode

if __name__ == "__main__":

    url = argv[1]
    email = argv[2]
    params = {"email": email}
    data = urlencode(params).encode('utf-8')

    req = Request(url, data)

    with urlopen(req) as res:

        print(f'{res.read().decode("utf-8")}')
