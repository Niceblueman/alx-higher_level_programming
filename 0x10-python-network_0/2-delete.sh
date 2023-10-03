#!/bin/bash
# Send a DELETE request to the specified URL and display the response body.
url="$1" && response_body=$(curl -sX DELETE "$url")
printf "%s" "$response_body"