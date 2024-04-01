#!/bin/bash
# send a POST request with content of a json file as its paylood
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
