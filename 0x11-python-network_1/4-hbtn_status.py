#!/usr/bin/python3

"""This script sends an HTTP GET request to a specified URL using the
requests library and prints information about the response received.
"""

import requests

if __name__ == "__main__":

    res = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print(f"\t- type: {type(res.text)}")
    print(f"\t- content: {res.text}")
