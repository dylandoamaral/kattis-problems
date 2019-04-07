#! /usr/bin/python3

import sys

line = sys.stdin.readline().strip().split()
limit = int(line[0])
n = int(line[1])

nop = 0
inside = 0

for i in range(0, n):
    line = sys.stdin.readline().strip().split()
    coming = int(line[1])
    if line[0] == 'enter':
        if inside + coming <= limit:
            inside += coming
        else:
            nop += 1
    else:
        inside -= coming

print(nop)