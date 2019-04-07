#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())
canisters = sorted(list(map(int, sys.stdin.readline().strip().split())))

factor = 0
mini = 1
explode = False
for i in range(0, n):
    if canisters[i] > (i + 1):
        explode = True
        break
    factor = 1 - ((i + 1) - canisters[i]) / (i + 1)
    if factor < mini:
        mini = factor

if explode:
    print("impossible")
else:
    print(mini)