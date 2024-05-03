#!/usr/bin/python3
"""Fetch a url vie the requests package"""
import requests


if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    result = response.text
    print("Body response:")
    print(f"\t- type: {type(result)}")
    print(f"\t- content: {result}")
