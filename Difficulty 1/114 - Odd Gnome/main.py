#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())
for i in range(0, n):
    gnomes = list(map(int, sys.stdin.readline().strip().split()))[1:]
    king = -1
    for i in range(1, len(gnomes) - 1):
        if gnomes[i] != gnomes[i - 1] + 1:
            king = i
            break;
    print(king + 1)
