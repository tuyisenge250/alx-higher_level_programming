#!/usr/bin/python3
"""
a script
sends a post request to the passing url
display the body of response"""

if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.parse

    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as resp:
        print(resp.read().decode("utf8"))