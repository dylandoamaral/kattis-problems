#! /usr/bin/python3

import sys
import math

line = sys.stdin.readline().strip().split()
while int(line[0]) != 0 and int(line[1]) != 0:
    D = int(line[0])
    V = int(line[1])
    D_area = math.pi * (D / 2) ** 2 * D
    d_area = D_area - V
    d = ((d_area - (1/12) * math.pi * D ** 3) * 48/(math.pi*8)) ** (1/3)
    print("{0:.6f}".format(d))
    line = sys.stdin.readline().strip().split()