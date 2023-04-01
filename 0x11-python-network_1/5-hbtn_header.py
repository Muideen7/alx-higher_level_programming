#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL
"""
import sys
import requests

if __name__ == "__main__":
    link = sys.argv[1]
    response = requests.get(url=link)
    print(response.headers.get('X-Request-Id'))
