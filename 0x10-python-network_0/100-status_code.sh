#!/bin/bash
# Send a request to the specified URL and display only the status code of the response.
url="$1" && curl -sI "$url" -o test7
awk 'NR==1{printf "%s", $2}' test7