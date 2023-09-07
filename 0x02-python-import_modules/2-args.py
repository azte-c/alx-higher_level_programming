#!/usr/bin/python3

if __name__ == "__main__":
    """number of arguments and list of arguments"""
    import sys

    num = len(sys.argv) - 1
    if num  == 0:
        print("0 arguments.")
    elif num == 1:
        print("1 argument.")
    else:
        print("{} arguments:" .format(num))

    for x in range(num):
        print("{}: {}" .format(x + 1, sys.argv[x + 1]))
