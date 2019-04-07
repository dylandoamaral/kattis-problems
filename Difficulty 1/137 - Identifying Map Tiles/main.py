#! /usr/bin/python3

import sys

data = sys.stdin.readline().strip()

zoom = len(data)
(x, y) = (0, 0)

for coord in data:
    (x, y) = (x * 2, y * 2)
    if coord == "1":
        (x, y) = (x + 1, y)
    elif coord == "2":
        (x, y) = (x, y + 1)
    elif coord == "3":
        (x, y) = (x + 1, y + 1)
    elif coord == "0":
        (x, y) = (x, y)

print(zoom, x, y)
