#!/bin/bash
# Send a request to the specified URL and display only the status code of the response.
awk 'NR==1{printf "%s", $2}' test7 $(curl -sI "$1" -o test7)
