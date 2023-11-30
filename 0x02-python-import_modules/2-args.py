#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 argement")
    elif count == 1:
        print("{} argument:\n{}:{}".format(count,count,sys.argv[1]))
    else :
        print("{} arguments:".format(count))
        for w in range(count):
            print("{}:{}".format(w + 1,sys.argv[w + 1]))
