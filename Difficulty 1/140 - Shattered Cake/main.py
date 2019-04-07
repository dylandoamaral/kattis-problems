#! /usr/bin/python3

import sys

wB = int(sys.stdin.readline())
n = int(sys.stdin.readline())

total = 0

for i in range(0, n):
    (w, h) = map(int, sys.stdin.readline().strip().split())
    total += w * h

print(int(total / wB))
