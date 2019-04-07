#! /usr/bin/python3

import sys

best = 0
result = 0

for i in range(1, 6):
    data = sys.stdin.readline().strip().split()
    total = 0
    for j in data:
        total += int(j)
    if total > result:
        best = i
        result = total
print(best, result)