#! /usr/bin/python3

import sys

text = sys.stdin.readline().strip()

total = len(text)
types = [0, 0, 0, 0]
for i in text:
    if i == '_':
        types[0] += 1
    elif 'a' <= i <= 'z':
        types[1] += 1
    elif 'A' <= i <= 'Z':
        types[2] += 1
    else:
        types[3] += 1

for i in range(0, 4):
    print('{0:.6f}'.format(types[i]/total))