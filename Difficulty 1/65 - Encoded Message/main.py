#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())

for i in range(0, n):
    line = sys.stdin.readline().strip()
    square = int(len(line) ** (1 / 2))
    splitted = [line[j:j+square] for j in range(0, len(line), square)]
    result = ""
    for j in range(square - 1, -1, -1):
        for k in range(0, square):
            result += splitted[k][j]
    print(result)