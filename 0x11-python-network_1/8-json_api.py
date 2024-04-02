#!/usr/bin/python3
"""Make a post request to a url with a given param and print the result
in certain format if any"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]

    res = requests.post(url, data={"q": q})
    try:
        data = res.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
