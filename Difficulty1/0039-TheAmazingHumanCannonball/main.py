#! /usr/bin/python3

import sys
import math

n = int(sys.stdin.readline().strip())

for i in range(0, n):
    line = sys.stdin.readline().strip().split()
    v0 = float(line[0])
    angle = math.radians(float(line[1]))
    x1 = float(line[2])
    h1 = float(line[3])
    h2 = float(line[4])
    t = x1 / (v0 * math.cos(angle))
    h = (v0 * t * math.sin(angle)) - ((1 / 2) * 9.81 * (t ** 2))
    if h1 + 1 < h < h2 - 1:
        print("Safe")
    else:
        print('Not Safe')
