#! /usr/bin/python3

import sys

line = sys.stdin.readline().strip().split()
N = int(line[0])
Q = int(line[1])

companies_location = sys.stdin.readline().strip().split()

for i in range(0, Q):
    line = sys.stdin.readline().strip().split()
    command = int(line[0])
    if command == 1:
        companies_location[int(line[1]) - 1] = line[2]
    else:
        print(abs(int(companies_location[int(line[1]) - 1]) - int(companies_location[int(line[2]) - 1])))