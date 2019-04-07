#! /usr/bin/python3

import sys
import math

n = sys.stdin.readline().strip().split()
roof = int(n[0])
angle = math.radians(int(n[1]))

print(math.trunc(roof/(math.sin(angle))) + 1)