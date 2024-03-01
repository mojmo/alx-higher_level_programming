#!/usr/bin/python3
"""This script sends a POST request to a web server and prints
search results if any are found.
"""
from sys import argv
import requests

if __name__ == "__main__":

    if len(argv) == 1:
        c = ""
    else:
        c = argv[1]

    values = {"q": c}
    r = requests.post(
        "http://16a435770e75.d82e1789.alx-cod.online:5000/search_user",
        data=values
    )

    try:
        json_res = r.json()
        if json_res == {}:
            print("No result")
        else:
            print(f'[{json_res.get("id")}] {json_res.get("name")}')
    except ValueError:
        print("Not a valid JSON")
