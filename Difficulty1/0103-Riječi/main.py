#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())

(A, B) = (0, 1)

for i in range(1, n):
    A, B = B, A + B

print(A, B)