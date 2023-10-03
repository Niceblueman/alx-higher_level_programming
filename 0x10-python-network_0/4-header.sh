#!/bin/bash
# Send a GET request to the specified URL with a custom header variable.
url="$1" && header="X-School-User-Id: 98"
response=$(curl -sH "$header" "$url") && printf "%s" "$response"