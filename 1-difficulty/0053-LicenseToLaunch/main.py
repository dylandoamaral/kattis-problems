#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())

lines = sys.stdin.readline().strip().split()
best = 0
for i in range(0, len(lines)):
    if int(lines[i]) < int(lines[best]):
        best = i
print(best)

