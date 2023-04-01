#!/usr/bin/python3
""" post email """
import requests
import sys

if __name__ == '__main__':
    link = sys.argv[1]
    email = {"email": sys.argv[2]}

    response = requests.get(url=link, data=email)
    print(response.text)
