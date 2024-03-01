#!/usr/bin/python3
"""retrieves the latest 10 commits from a GitHub repository.

Usage: ./100-github_commits.py <repository> <owner>
"""
from sys import argv
import requests

if __name__ == "__main__":
    res = requests.get("https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1]
    ))
    json_res = res.json()

    try:
        for i in range(10):
            print('{}: {}'.format(
                json_res[i].get("sha"),
                json_res[i].get("commit").get("author").get("name")
            ))
    except IndexError:
        pass
