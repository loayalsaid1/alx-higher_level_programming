#!/bin/bash
# Make a POST request to the URL given sending extra parameters with the request
curl -s -H POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
