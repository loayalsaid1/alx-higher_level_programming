#!/usr/bin/python3
"""Get an email as a parameter and send it as a
    parameter in the body"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    parameter = {"email": argv[2]}

    response = requests.post(url, data=parameter)
    print(response.text)
