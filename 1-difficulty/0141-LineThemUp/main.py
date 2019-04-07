#! /usr/bin/python3

import sys


def isSame(normal, sorted):
    for i in range(0, len(normal)):
        if normal[i] != sorted[i]:
            return False
    return True


n = int(sys.stdin.readline())
names = []
for i in range(0, n):
    names.append(sys.stdin.readline().strip())

inc = names.copy()
inc.sort()
dec = names.copy()
dec.sort(reverse = True)

if isSame(names, inc):
    print("INCREASING")
elif isSame(names, dec):
    print("DECREASING")
else:
    print("NEITHER")
