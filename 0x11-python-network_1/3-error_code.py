#!/usr/bin/python3
"""
rite a Python script that takes in a URL, sends a request to the URL and displays the body of the respons

"""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    link = sys.argv[1]

    response = urllib.request.Request(link)

    try:
        with urllib.request.urlopen(response) as res:
            print(res.read().decode('ascii'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

