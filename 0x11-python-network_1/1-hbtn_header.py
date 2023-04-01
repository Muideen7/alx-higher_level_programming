#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


if __name__ == "__main__":
    link = sys.argv[1]

    request = urllib.request.Request(link)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
