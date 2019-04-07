#! /usr/bin/python3

import sys

n = int(sys.stdin.readline())

moy = 0
m = 0
for i in range(0, n):
    minutes, reality = map(int, sys.stdin.readline().strip().split())
    m += minutes
    moy += (reality / 60)

res = moy / m
if res <= 1:
    print("measurement error")
else:
    print("{0:.8f}".format(res))