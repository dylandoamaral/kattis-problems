#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())

for i in range(0, n):
    m = int(sys.stdin.readline().strip())
    cities = []
    for j in range(0, m):
        cities.append(sys.stdin.readline().strip())
    print(len(set(cities)))