#! /usr/bin/python3

import sys


line = list(map(int, sys.stdin.readline().strip().split()))

previous = -1
found = []


for i in range(0, line[1]):
    a = int(sys.stdin.readline().strip())
    found.append(a)

found = set(found)
for j in range(0, line[0]):
    if j not in found:
        print(j)

print("Mario got " + str(len(found)) + " of the dangerous obstacles.")