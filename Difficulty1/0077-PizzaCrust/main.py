#! /usr/bin/python3

import sys
import math


line = sys.stdin.readline().strip().split()
R = int(line[0])
C = int(line[1])

areaMax = math.pi * R ** 2
areaInside = math.pi * (R - C) ** 2
print("{0:.6f}".format((areaInside * 100) / areaMax))