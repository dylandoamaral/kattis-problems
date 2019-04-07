#! /usr/bin/python3

import sys

line = sys.stdin.readline().strip().split()

R = int(line[0])
C = int(line[1])
N = int(line[2])

map = [[0 for x in range(C)] for y in range(R)]
conquered = 0

controlled = []
next = []

day = 1

for i in range(0, N):
    line = sys.stdin.readline().strip().split()
    X = int(line[0]) - 1
    Y = int(line[1]) - 1
    if map[X][Y] != 1:
        conquered += 1
    map[X][Y] = 1
    controlled.append((X, Y))

while conquered != R * C:
    for zone in controlled:
        if zone[0] - 1 >= 0 and map[zone[0] - 1][zone[1]] == 0:
            map[zone[0] - 1][zone[1]] = 1
            next.append((zone[0] - 1, zone[1]))
            conquered += 1
        if zone[0] + 1 < R and map[zone[0] + 1][zone[1]] == 0:
            map[zone[0] + 1][zone[1]] = 1
            next.append((zone[0] + 1, zone[1]))
            conquered += 1
        if zone[1] - 1 >= 0 and map[zone[0]][zone[1] - 1] == 0:
            map[zone[0]][zone[1] - 1] = 1
            next.append((zone[0], zone[1] - 1))
            conquered += 1
        if zone[1] + 1 < C and map[zone[0]][zone[1] + 1] == 0:
            map[zone[0]][zone[1] + 1] = 1
            next.append((zone[0], zone[1] + 1))
            conquered += 1
    controlled = next.copy()
    next.clear()
    day += 1

print(day)
