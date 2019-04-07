#! /usr/bin/python3

import sys

line = sys.stdin.readline().strip().split()

x = int(line[0])
y = int(line[1])

map = []
count = [0, 0, 0, 0, 0]

for i in range(0, x):
    line = sys.stdin.readline().strip()
    map.append(line)

for i in range(0, x - 1):
    for j in range(0, y - 1):
        cases = [map[i][j], map[i + 1][j], map[i][j + 1], map[i + 1][j + 1]]
        if cases[0] == "#" or cases[1] == "#" or cases[2] == "#" or cases[3] == "#":
            continue
        count[cases.count("X")] += 1

for i in count:
    print(i)
