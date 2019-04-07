#! /usr/bin/python3

import sys

n = int(sys.stdin.readline())
prevLine = sys.stdin.readline().strip().split()
total = 0
for sample in range(1, n):

    line = sys.stdin.readline().strip().split()
    total += (float(prevLine[1]) + float(line[1]))/2*(float(line[0]) - float(prevLine[0]))
    prevLine = line
print("{0:.6f}".format(total/1000))
