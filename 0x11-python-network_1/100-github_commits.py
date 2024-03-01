#!/usr/bin/python3
"""This script retrieves the latest 10 commit SHAs and their authors
from a GitHub repository.

Usage: ./100-github_commits.py <repository> <owner>
"""
from sys import argv
import requests

if __name__ == "__main__":
    res = requests.get(f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits")
    json_res = res.json()

    try:
        for i in range(10):
            author = json_res[i].get("commit").get("author").get("name")
            sha = json_res[i].get("sha")
            print(f'{sha}: {author}')
    except IndexError:
        pass
