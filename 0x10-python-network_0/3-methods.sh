#!/bin/bash
# Print all the allowed HTTP requests on specifc resource on a server
curl -sI "$1" | sed -n "/Allow: /s/Allow: //p"
