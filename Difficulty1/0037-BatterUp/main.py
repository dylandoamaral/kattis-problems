#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip().split()

total = 0
for i in line:
    if int(i) < 0:
        n -= 1
    else:
        total += int(i)

print(total / n)