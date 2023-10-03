#!/bin/bash
# Calculate the byte size of the HTTP response header for a specified URL.
url="$1" && header_size=$(curl -s "$url" | wc -c)
echo "$header_size"