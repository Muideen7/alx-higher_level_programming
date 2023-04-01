#!/bin/bash
# Write a Bash script that show the size of an HTTP requests
curl -s "$1" | wc -c
