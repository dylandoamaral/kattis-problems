#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())
oddities = ['even', 'odd']
for i in range(0, n):
    n = int(sys.stdin.readline().strip())
    print(n, 'is', oddities[n % 2])