#! /usr/bin/python3

import sys

p, n = map(int, sys.stdin.readline().strip().split())
d = []
day = 0
for i in range(0, n):
    day += 1
    w = sys.stdin.readline().strip()
    if w not in d:
        d.append(w)
    if len(d) == p:
        break;

if len(d) == p:
    print(day)
else:
    print("paradox avoided")
