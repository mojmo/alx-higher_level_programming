#!/usr/bin/python3

"""This script sends an HTTP GET request to a specified URL
and prints information about the response received.

The script sends an HTTP GET request to https://alx-intranet.hbtn.io/status
and prints the following information:

- Type of the response body (bytes)
- Content of the response body (bytes)
- Content of the response body as a UTF-8 decoded string
"""

from urllib.request import urlopen

if __name__ == "__main__":

    with urlopen("https://alx-intranet.hbtn.io/status") as res:
        res_body = res.read()
        print('Body response:')
        print(f'\t- type: {type(res_body)}')
        print(f'\t- content: {res_body}')
        print(f'\t- utf8 content: {res_body.decode("UTF-8")}')
