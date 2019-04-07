#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())
while n != -1:
    previousT = 0
    total = 0
    for i in range(0, n):
        line = sys.stdin.readline().strip().split()
        V = int(line[0])
        T = int(line[1])
        T = T - previousT
        total += T * V
        previousT += T
    print(total, "miles")
    n = int(sys.stdin.readline().strip())
