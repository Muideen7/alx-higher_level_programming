#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    response = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(response) as res:
        body = res.read()
        print("Body response:")
        print(f'\t- type: {type(body)}')
        print(f'\t- content: {body}')
        print(f'\t- utf8 content: {body.decode("utf-8")}')
