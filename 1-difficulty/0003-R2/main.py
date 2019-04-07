#! /usr/bin/python3

import sys

line = sys.stdin.readline().strip().split()
r1 = int(line[0])
mean = int(line[1])
r2 = mean * 2 - r1
print(r2)