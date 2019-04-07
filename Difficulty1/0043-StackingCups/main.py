#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())

cups = dict()
for i in range(0, n):
    line = sys.stdin.readline().strip().split()
    color = ""
    radius = 0
    if line[0].isdigit():
        color = line[1]
        radius = int(line[0]) / 2
    else:
        color = line[0]
        radius = int(line[1])
    cups[color] = radius

sorted_cups = sorted(cups.items(), key=lambda kv: kv[1])

for e in sorted_cups:
    print(e[0])
