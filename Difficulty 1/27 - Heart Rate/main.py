#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())

for i in range(0, n):
    line = sys.stdin.readline().strip().split()
    b = int(line[0])
    p = float(line[1])
    _mid = (60 * b) / p
    _min = (60 * (b - 1)) / p
    _max = (60 * (b + 1)) / p
    print("{0:.4f}".format(_min), "{0:.4f}".format(_mid), "{0:.4f}".format(_max))