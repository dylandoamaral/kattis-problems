#! /usr/bin/python3

import sys

price = float(sys.stdin.readline().strip())
number_lawns = int(sys.stdin.readline().strip())
total = 0

for i in range(0, number_lawns):
    line = sys.stdin.readline().strip().split()
    w = float(line[0])
    h = float(line[1])
    total += w * h * price

print("{0:.6f}".format(total))