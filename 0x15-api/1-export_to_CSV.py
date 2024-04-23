#!/usr/bin/python3
"""Use an api"""
import requests
import json
import sys
try:
    user_id = sys.argv[1]
except Exception:
    exit()

user = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
user = json.loads(user.text)

tasks = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{user_id}/todos")
tasks = json.loads(tasks.text)

titles = [task['title'] for task in tasks]


with open('USER_ID.csv', 'a'):
    name = user['name']
    
