#!/usr/bin/python3
"""use the github api with basic autintication to get user id"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (argv[1], argv[2])

    res = requests.get(url, auth=auth)
    if (res.status_code == 200):
        data = res.json()
        print(data['id'])
    else:
        print(None)
