#! /usr/bin/python3

import sys

m, n = map(int, sys.stdin.readline().strip().split())

if m < 8:
    print("unsatisfactory")
else:
    print("satisfactory")