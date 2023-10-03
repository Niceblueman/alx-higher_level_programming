#!/bin/bash
# Make a request to the URL fe2aca13d8ab.32fb08c5.alx-cod.online:5000/catch_me to retrieve the message "You got me!".
url="0.0.0.0:5000/catch_me" && request_data="user_id=98" && curl -sL -X PUT -H "Origin: School" -d "$request_data" "$url"
