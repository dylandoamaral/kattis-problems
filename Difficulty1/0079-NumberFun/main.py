#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())

for i in range(0, n):
    line = sys.stdin.readline().strip().split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])

    if a + b == c:
        print("possible")
    elif abs(a - b) == c:
        print("possible")
    elif a * b == c:
        print("possible")
    elif a / b == c:
        print("possible")
    elif b / a == c:
        print("possible")
    else:
        print("impossible")
