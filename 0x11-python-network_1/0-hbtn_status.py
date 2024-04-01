#!/usr/bin/python3
"""Fetch a url vie the urllib package"""
from urllib.request import urlopen


with urlopen('https://alx-intranet.hbtn.io/status') as response:
    result = response.read()
    print("Body response:")
    print(f"\t- type: {type(result)}")
    print(f"\t- content: {result}")
    print(f"\t- utf8 content: {result.decode('utf-8')}")
