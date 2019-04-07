#! /usr/bin/python3

import sys


def find_coord(tab):
    for i in tab:
        if tab.count(i) == 1:
            return i


line = sys.stdin.readline().strip().split()
x_1, y_1 = int(line[0]), int(line[1])
line = sys.stdin.readline().strip().split()
x_2, y_2 = int(line[0]), int(line[1])
line = sys.stdin.readline().strip().split()
x_3, y_3 = int(line[0]), int(line[1])

xs = [x_1, x_2, x_3]
ys = [y_1, y_2, y_3]

x_4, y_4 = find_coord(xs), find_coord(ys)
print(x_4, y_4)