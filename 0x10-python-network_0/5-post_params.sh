#!/bin/bash
# Send a POST request to the specified URL and display the response body.
url="$1" && post_data="email=test@gmail.com&subject=I will always be here for PLD" && response=$(curl -s "$url" -X POST -d "$post_data") && printf "%s" "$response"
