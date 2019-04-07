#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())

res = 0
fac = 1

for i in range(0, n + 1):
    if i > 1:
        fac = fac * i
    res += (1 / fac)
print(res)