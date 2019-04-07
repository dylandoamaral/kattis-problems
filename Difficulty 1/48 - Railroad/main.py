#! /usr/bin/python3

import sys

line = sys.stdin.readline().strip().split()
X = int(line[0])
Y = int(line[1])

if (X * 4 + Y * 3) % 2 == 0:
    print("possible")
else:
    print("impossible")