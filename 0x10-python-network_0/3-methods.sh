#!/bin/bash
# Fetch and display the supported HTTP methods for a specified URL.
url="$1" && http_methods=$(curl -Is "$url" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev) && printf "%s" "$http_methods"
