#!/bin/bash
# Make a requst to a URL and add a header variable to to reqeuest header
curl -s -H "X-School-User-Id: 98" "$1"
