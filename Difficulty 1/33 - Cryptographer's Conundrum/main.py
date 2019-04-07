#! /usr/bin/python3

import sys

cipher = sys.stdin.readline().strip()
total = 0
for i in range(0, len(cipher)):
    if i % 3 == 0:
        if cipher[i] != "P":
            total += 1
    elif i % 3 == 1:
        if cipher[i] != "E":
            total += 1
    else:
        if cipher[i] != "R":
            total += 1
print(total)