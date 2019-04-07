#! /usr/bin/python3

import sys


moves = sys.stdin.readline().strip()
left, middle, right = 1, 0, 0

for i in moves:
    if i == "A":
        left, middle, right = middle, left, right
    elif i == 'B':
        left, middle, right = left, right, middle
    else:
        left, middle, right = right, middle, left

res = left, middle, right
print(res.index(max(res)) + 1)
