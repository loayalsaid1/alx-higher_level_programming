#!/usr/bin/python3
"""
    Get the header of a url request responser
    Make sinse, right? :)
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
