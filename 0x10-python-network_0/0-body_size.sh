#!/bin/bash
#sends get request and display response
curl -s "$1" | wc -c
