#!/usr/bin/python3

if __name__ == "__main__":
    """addition of all the argumrnts passed"""
    import sys

    count = 0
    for x in range(len(sys.argv) - 1):
        count += int(sys.argv[x + 1])
    print("{}" .format(count))
