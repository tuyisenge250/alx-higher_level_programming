#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
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
