#! /usr/bin/python3

import sys

information = list(map(int, sys.stdin.readline().strip().split()))
N = information[0]
P = information[1]
Q = information[2]

total = P + Q

if total % (N * 2) < N:
    print("paul")
else:
    print("opponent")
