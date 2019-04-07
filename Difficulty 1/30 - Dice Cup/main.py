#! /usr/bin/python3

import sys

n = sys.stdin.readline().strip().split()
dice_one = int(n[0])
dice_two = int(n[1])

possibilities = dict()

for i in range(1, dice_one + 1):
    for j in range(1, dice_two + 1):
        if i + j in possibilities:
            possibilities[i + j] += 1
        else:
            possibilities[i + j] = 1

maximum = possibilities[max(possibilities, key=possibilities.get)]

for key, value in possibilities.items():
    if value == maximum:
        print(key)