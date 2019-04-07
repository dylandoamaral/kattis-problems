#! /usr/bin/python3

import sys

values = sys.stdin.readline().strip().split()
for i in range(0, len(values)):
    values[i] = values[i][0]

unique = set(values)
res = 0
for i in unique:
    occ = values.count(i)
    if occ > res:
        res = occ

print(res)