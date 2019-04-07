#! /usr/bin/python3

import sys
import math

values = sys.stdin.readline().strip().split()

N = int(values[0])
W = int(values[1])
H = int(values[2])

hypothenus = math.sqrt(W ** 2 + H ** 2)

for i in range(0, N):
    length = int(sys.stdin.readline().strip())
    if length > hypothenus:
        print("NE")
    else:
        print("DA")