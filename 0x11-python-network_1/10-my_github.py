#!/usr/bin/python3

"""Retrieves and prints the user ID of a GitHub user using
Basic Authentication.

Arguments:
- <username> (str): The GitHub username.
- <password> (str): The GitHub password or an access token.

Usage: ./10-my_github.py <username> <password>
"""

from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = argv[1]
    passwd = argv[2]

    basic_auth = HTTPBasicAuth(username, passwd)

    res = requests.get("https://api.github.com/user", auth=basic_auth)
    json_res = res.json()

    print(json_res.get("id"))
