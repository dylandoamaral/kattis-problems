#! /usr/bin/python3

import sys

N = int(sys.stdin.readline().strip())

points = 4
bottom_points = 2
for i in range(0, N):
    superposition = ((bottom_points - 1) * 8) + 4
    truth = 4 * (bottom_points - 1) + 1
    similar = superposition - truth
    points = points * 4 - similar
    bottom_points = 2 * bottom_points - 1
print(points)