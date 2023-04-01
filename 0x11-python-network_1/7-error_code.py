#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    link = sys.argv[1]

    response = requests.get(url=link)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
