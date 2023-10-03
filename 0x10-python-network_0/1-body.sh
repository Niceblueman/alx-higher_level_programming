#!/bin/bash
# Send a GET request to the specified URL and display the response body.
url="$1" && response_body=$(curl -sL "$url")
printf "%s" "$response_body"