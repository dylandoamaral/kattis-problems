#! /usr/bin/python3

import sys
import math

line = sys.stdin.readline().strip().split()
r = float(line[0])
m = int(line[1])
c = int(line[2])

while r != 0 or m !=0 or c != 0:
    tmp = c / m
    print("{0:.5f}".format(math.pi * r ** 2), "{0:.5f}".format(tmp * ((r * 2) ** 2)))
    line = sys.stdin.readline().strip().split()
    r = float(line[0])
    m = int(line[1])
    c = int(line[2])
