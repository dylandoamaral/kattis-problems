#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())

for i in range(0, n):
    stores = int(sys.stdin.readline().strip())
    positions = sys.stdin.readline().strip().split()
    total = 0
    for pos in range(0, stores):
        positions[pos] = int(positions[pos])
        total += positions[pos]
    total /= stores
    distance = total - min(positions)
    distance += max(positions) - min(positions)
    distance += max(positions) - total
    print(int(distance))