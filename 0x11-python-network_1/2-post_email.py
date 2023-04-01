#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    link = sys.argv[1]
    rec = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(rec).encode("ascii")

    response = urllib.request.Request(link, data)
    with urllib.request.urlopen(response) as res:
        print(res.read().decode('utf-8'))
