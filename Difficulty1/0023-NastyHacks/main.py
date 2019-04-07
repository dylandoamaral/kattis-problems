#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())

for i in range(0, n):
    n = sys.stdin.readline().strip().split()
    r = int(n[0])
    e = int(n[1])
    c = int(n[2])
    cal = r - (e - c)
    if cal == 0:
        print("does not matter")
    elif cal > 0:
        print("do not advertise")
    else:
        print("advertise")