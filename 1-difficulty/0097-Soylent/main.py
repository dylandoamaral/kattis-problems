#! /usr/bin/python3

import sys
import math

n = int(sys.stdin.readline().strip())

for i in range(0, n):
    a = int(sys.stdin.readline().strip())
    print(math.ceil(a / 400))
