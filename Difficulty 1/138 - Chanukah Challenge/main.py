#! /usr/bin/python3

import sys

n = int(sys.stdin.readline())

res = [2]

for i in range(0, n):
    (num, days) = map(int, sys.stdin.readline().strip().split())
    if len(res) < days:
        for j in range(len(res), days + 1):
            res.append(res[-1] + 1)
    print(num, sum(res[0:days]))
