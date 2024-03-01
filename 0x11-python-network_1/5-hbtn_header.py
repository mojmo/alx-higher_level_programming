#!/usr/bin/python3
"""This script sends an HTTP GET request to a specified URL using the
requests library and prints the value of the 'X-Request-Id' header
from the response.

Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))
