#!/usr/bin/python3
"""
A script takes URL
sends request to the URL
diplay body"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error

    url= sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as res:
            print(res.read().decode("UTF-8"))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)