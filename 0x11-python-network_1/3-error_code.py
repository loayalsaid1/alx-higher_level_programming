#!/usr/bin/python3
"""Sedn a request to a url,
    print it on success and print the error code if there is a HTTPError
"""
import urllib.error
import urllib.request
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
