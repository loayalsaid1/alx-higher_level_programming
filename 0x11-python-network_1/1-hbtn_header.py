#!/usr/bin/python3
"""Get the header of a url request responser"""
from urllib.request import urlopen
from sys import argv


with urlopen(argv[1]) as response:
    print(response.headers['X-Request-Id'])
