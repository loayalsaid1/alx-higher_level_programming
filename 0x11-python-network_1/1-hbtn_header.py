#!/usr/bin/python3
"""
    Get the header of a url request responser
    Make sinse, right? :)
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers["X-Request-Id"])
