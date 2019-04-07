#! /usr/bin/python3

import sys


def dist(p, q):
    return round(((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** (1/2))


def naif(points):
    tour = [0 for i in range(len(points))]
    used = [False for i in range(len(points))]
    used[0] = True
    for i in range(1, len(points)):
        best = -1
        for j in range(0, len(points)):
            if used[j] is False and (best == -1 or dist(points[tour[i - 1]], points[j]) < dist(points[tour[i - 1]], points[best])):
                best = j
        tour[i] = best
        used[best] = True
    return tour


n = int(sys.stdin.readline().strip())
points = []
for i in range(0, n):
    line = sys.stdin.readline().strip().split()
    x = float(line[0])
    y = float(line[1])
    points.append((x, y))

for i in naif(points):
    print(i)