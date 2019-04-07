#! /usr/bin/python3

import sys
import math

while True:
    (w, h, s, m, n) = map(int, sys.stdin.readline().strip().split())
    if w == 0 and h == 0 and s == 0 and m == 0 and n == 0:
        break;
    hypo = math.sqrt((m * w) ** 2 + (n * h) ** 2)

    speed = (hypo / s)
    angle = math.asin((n * h) / hypo)
    angle = math.degrees(angle)

    print("{0:.2f}".format(angle), "{0:.2f}".format(speed))