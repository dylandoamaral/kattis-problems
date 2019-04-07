#! /usr/bin/python3

import sys

dimensions = list(map(int, sys.stdin.readline().strip().split()))
R = dimensions[0]
S = dimensions[1]
K = dimensions[2]

grid = []
for i in range(0, R):
    grid.append(list(sys.stdin.readline().strip()))

maxFlies = -1
flies = 0
(row, col) = (-1, -1)

for i in range(0, R - K + 1):
    for j in range(0, S - K + 1):
        flies = 0
        for ki in range(i + 1, i + K - 1):
            for kj in range(j + 1, j + K - 1):
                if grid[ki][kj] == "*":
                    flies += 1
        if flies > maxFlies:
            maxFlies = flies
            (row, col) = (i, j)

grid[row][col] = "+"
grid[row + K - 1][col] = "+"
grid[row][col + K - 1] = "+"
grid[row + K - 1][col + K - 1] = "+"
for i in range(row + 1, row + K - 1):
    grid[i][col] = "|"
    grid[i][col + K - 1] = "|"
for j in range(col + 1, col + K - 1):
    grid[row][j] = "-"
    grid[row + K - 1][j] = "-"

print(maxFlies)
for i in grid:
    print(''.join(i))