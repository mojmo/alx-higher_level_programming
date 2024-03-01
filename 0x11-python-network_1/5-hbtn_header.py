#!/usr/bin/python3
"""Prints the value of the 'X-Request-Id' header from the response.

Usage: ./5-hbtn_header.py <URL>
"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get("X-Request-Id"))
