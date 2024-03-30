#!/bin/bash
# Get the size of a body of a get HTTP response
curl -si $1 | grep "Content-Length" | cut --delimiter=" " --fields=2
