#!/usr/bin/python3
"""Get a header variable from the headervalues return by the server
after making a request
"""
from urllib.request import urlopen
from sys import argv


with urlopen(argv[1]) as response:
    print(response.headers['X-Request-Id'])
