#!/bin/bash
# sends json and post request body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
