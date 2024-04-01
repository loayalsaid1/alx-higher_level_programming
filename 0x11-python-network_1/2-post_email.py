#!/usr/bin/python3
"""Get an email as a parameter and send it as a
    parameter in the body"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    parameter = {"email": argv[2]}

    data = urlencode(parameter)
    data = data.encode('ascii')

    request = Request(url, data)
    with urlopen(request) as response:
        print(response.read().decode('utf-8'))
