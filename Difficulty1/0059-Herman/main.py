#! /usr/bin/python3

import sys
import math


def area(R):
    return math.pi * R ** 2


def dist_toxicab(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


n = int(sys.stdin.readline().strip())

R_euclid = n
R_taxicab = n * math.sqrt(2) / math.sqrt(math.pi)

print("{0:.6f}".format(area(R_euclid)))
print("{0:.6f}".format(area(R_taxicab)))