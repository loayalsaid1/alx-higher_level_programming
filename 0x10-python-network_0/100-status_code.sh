#!/bin/bash
# Print the status code of a request to given URL
curl -s -o /dev/null -w "%{http_code}" "$1"
