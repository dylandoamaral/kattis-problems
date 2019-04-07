#! /usr/bin/python3

import sys
import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


line = sys.stdin.readline().strip().split()

x, y = int(line[0]), int(line[1])
x1, y1 = int(line[2]), int(line[3])
x2, y2 = int(line[4]), int(line[5])

if x < x1 and y1 < y < y2:
    print("{0:.3f}".format(abs(x1 - x)))
elif x > x2 and y1 < y < y2:
    print("{0:.3f}".format(abs(x - x2)))
elif y < y1 and x1 < x < x2:
    print("{0:.3f}".format(abs(y1 - y)))
elif y > y2 and x1 < x < x2:
    print("{0:.3f}".format(abs(y - y2)))
elif x < x1 and y < y1:
    print("{0:.3f}".format(distance(x, y, x1, y1)))
elif x < x1 and y > y2:
    print("{0:.3f}".format(distance(x, y, x1, y2)))
elif x > x2 and y > y2:
    print("{0:.3f}".format(distance(x, y, x2, y2)))
else:
    print("{0:.3f}".format(distance(x, y, x2, y1)))