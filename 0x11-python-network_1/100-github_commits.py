#!/usr/bin/python3

"""This script retrieves the latest 10 commit SHAs and their authors
from a GitHub repository.

Arguments:
- <repository> (str): The name of the GitHub repository.
- <owner> (str): The owner or organization of the GitHub repository.

Usage: ./100-github_commits.py <repository> <owner>
"""

from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    repo = argv[1]
    owner = argv[2]

    res = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
    json_res = res.json()

    for i in range(10):
        author = json_res[i].get("commit").get("author").get("name")
        sha = json_res[i].get("sha")
        print(f'{sha}: {author}')
