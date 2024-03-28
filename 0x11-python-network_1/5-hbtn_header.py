#!/usr/bin/python3
"""script
sends request to url
and display X-Request-Id"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get('X-Request-Id'))