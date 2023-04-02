#!/usr/bin/bash
# sends a request to that URL, and displays 
# the size of the body of the response using cURL
curl -s "$1" | wc -c
