#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())

for i in range(0, n):
    line_1 = sys.stdin.readline().strip()
    print(line_1)
    line_2 = sys.stdin.readline().strip()
    print(line_2)
    for j in range(0, len(line_1)):
        if line_1[j] == line_2[j]:
            print(".", end='')
        else:
            print("*", end='')
    print("\n")
