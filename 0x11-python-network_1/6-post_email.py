#!/usr/bin/python3
"""This script sends a POST request to a specified URL with an 'email'
parameter and prints the response.

Usage: ./6-post_email.py <URL> <EMAIL>
"""
from sys import argv
import requests

if __name__ == "__main__":
    values = {"email": argv[2]}
    r = requests.post(argv[1], data=values)
    print(r.text)
