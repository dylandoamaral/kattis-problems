#! /usr/bin/python3

import sys
import math

def SSD(b, n):
    i = 0
    while b ** i <= n:
        i += 1
    power = i - 1
    total = 0
    residue = n
    for p in range(power, -1, -1):
        total += math.trunc(residue / b ** p) ** 2
        residue = residue % b ** p
    return total

n = int(sys.stdin.readline().strip())

for i in range(0, n):
    line = sys.stdin.readline().strip().split()
    k = int(line[0])
    b = float(line[1])
    n = int(line[2])
    print(k, SSD(b, n))
