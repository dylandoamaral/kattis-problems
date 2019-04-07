#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())

days = []

for i in range(0, n):
    line = sys.stdin.readline().strip().split()
    _from = int(line[0])
    _to = int(line[1])
    for day in range(_from, _to + 1):
        days.append(day)

print(len(set(days)))