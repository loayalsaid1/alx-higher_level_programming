#!/usr/bin/python3
"""Sedn a request to a url,
    print it on success and print the error code if there is an error
        <<Status code >= 400
"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get(argv[1])
    if response.ok:
        print(response.text)
    else:
        print("Error code:", response.status_code)
