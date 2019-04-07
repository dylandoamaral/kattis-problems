#! /usr/bin/python3

import sys


def sum(dwarfes, fake_1, fake_2):
    total = 0
    for i in range(0, 9):
        if i != fake_1 and i != fake_2:
            total += dwarves[i]
    return total


def find(dwarfes):
    for i in range(0, 9):
        for j in range(0, 9):
            if i != j:
                if sum(dwarves, i, j) == 100:
                    return i, j


dwarves = []
for i in range(0, 9):
    dwarves.append(int(sys.stdin.readline().strip()))

(f1, f2) = find(dwarves)

for i in range(0, 9):
    if i != f1 and i != f2:
        print(dwarves[i])
