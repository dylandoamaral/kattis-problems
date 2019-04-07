#! /usr/bin/python3

import sys


def distance(x1, y1, x2, y2, p):
    return (abs(x1 - x2) ** p + abs(y1 - y2) ** p) ** (1/p)


line = sys.stdin.readline().strip().split()

while len(line) > 1:
    x1 = float(line[0])
    y1 = float(line[1])
    x2 = float(line[2])
    y2 = float(line[3])
    p = float(line[4])
    print("{0:.5f}".format(distance(x1, y1, x2, y2, p)))
    line = sys.stdin.readline().strip().split()
