#!/usr/bin/python3
"""
a script
sends request to url
and display X-Request-Id"""

if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as res:
        print(dict(res.headers).get("X-Request-Id"))