#! /usr/bin/python3

import sys


def smallest(word_1, word_2):
    if len(word_1) < 2:
        return word_2
    elif len(word_2) < 2:
        return word_1
    n = len(word_1) if len(word_1) > len(word_2) else len(word_2)
    for i in range(0, n):
        if i == len(word_1):
            return word_1
        elif i == len(word_2):
            return word_2
        elif ord(word_1[i]) < ord(word_2[i]):
            return word_1
        elif ord(word_1[i]) > ord(word_2[i]):
            return word_2
    return word_1

dimensions = list(map(int, sys.stdin.readline().strip().split()))
R = dimensions[0]
C = dimensions[1]

grid = []
for i in range(0, R):
    grid.append(sys.stdin.readline().strip())

best = "xxxxxxxxxxxxxxxxxxxx"
for line in grid:
    for word in line.split("#"):
        best = smallest(best, word)


for i in range(0, C):
    line = ""
    for j in range(0, R):
        line += grid[j][i]
    for word in line.split("#"):
        best = smallest(best, word)

print(best)