#! /usr/bin/python3

import sys
import math

line = sys.stdin.readline().strip().split()

while int(line[0]) != 0 and int(line[1]) != 0:
    num = int(line[0])
    denum = int(line[1])
    print(math.trunc(num/denum), num % denum, "/", denum)
    line = sys.stdin.readline().strip().split()
