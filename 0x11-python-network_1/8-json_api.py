#!/usr/bin/python3
"""
script that takes a letter
use post to send request http://0.0.0.0:5000/search_user
letter is parameter pass to moduel
"""
import requests
import sys

if __name__ == "__main__":
    letter="" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter} 
    url = "http://0.0.0.0:5000/search_user"
    res= requests.post(url, data=payload)

    try:
        response = res.json()
        if response == {}:
            print('No result')
        else:
            print("[{}] {}".format(response.get("id"),response.get("name")))
    except ValueError:
        print("Not a valid JSON")
