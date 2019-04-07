#! /usr/bin/python3

import sys

matrix = []

line = sys.stdin.readline().strip().split()
R = int(line[0])
C = int(line[1])
Zr = int(line[2])
Zc = int(line[3])

for i in range(0, R):
    line = sys.stdin.readline().strip()
    evolution = ""
    for j in line:
        for k in range(0, Zc):
            evolution += j
    for j in range(0, Zr):
        print(evolution)

