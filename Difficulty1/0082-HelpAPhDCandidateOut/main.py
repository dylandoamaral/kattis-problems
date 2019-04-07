#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())

for i in range(0, n):
    try:
        line = sys.stdin.readline().strip().split('+')
        a = int(line[0])
        b = int(line[1])
        print(a + b)
    except:
        print("skipped")
