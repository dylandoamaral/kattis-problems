#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())

for i in range(0, n):
    line = sys.stdin.readline().strip().split()
    values = line[:-1]
    total = 0
    previous = int(values[0])
    for j in values[1:]:
        curr = int(j)
        if curr > previous * 2:
            total += curr - previous * 2
        previous = curr
    print(total)

