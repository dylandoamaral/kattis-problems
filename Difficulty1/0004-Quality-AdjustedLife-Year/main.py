#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())
total = 0
for i in range(0, n):
    line = sys.stdin.readline().strip().split()
    total += float(line[0]) * float(line[1])
print("{0:.3f}".format(total))