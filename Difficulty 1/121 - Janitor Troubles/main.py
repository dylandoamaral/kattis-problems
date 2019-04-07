#! /usr/bin/python3

import sys
import math

s1, s2, s3, s4 = map(int, sys.stdin.readline().strip().split())
semiperimeter = (s1 + s2 + s3 + s4) / 2

print(math.sqrt((semiperimeter - s1)*(semiperimeter - s2)*(semiperimeter - s3)*(semiperimeter - s4)))