#!/usr/bin/python3
"""
a script
sends a post request to the passing url
display the body of response"""

if __name__ == "__main__":
    import requests
    import sys

    value = {'email': sys.argv[2]}
    url = sys.argv[1]
    res = requests.post(url, data= value)
    print(f"Your email is:", dict(res.headers).get("X-Request-Id"))
    