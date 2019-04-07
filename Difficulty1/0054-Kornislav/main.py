#! /usr/bin/python3

import sys

lines = sys.stdin.readline().strip().split()
for i in range(0, len(lines)):
    lines[i] = int(lines[i])

lines = sorted(lines)
print(lines[0] * lines[2])
