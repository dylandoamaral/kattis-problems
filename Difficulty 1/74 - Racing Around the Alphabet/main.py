#! /usr/bin/python3

import sys
import math

n = int(sys.stdin.readline().strip())

tokens = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"

for i in range(0, n):
    line = sys.stdin.readline().strip()

    circumference = math.pi * 60
    step = circumference / 28 #feet to make between tokens

    total = 0
    position = tokens.index(line[0])

    for letter in line:
        goal = tokens.index(letter)
        distance = 0
        if goal > position:
            distance = goal - position
            potential = goal - 28 - position
            if abs(potential) < distance:
                distance = potential
        else:
            distance = -(position - goal)
            potential = -(position - 28 - goal)
            if potential < abs(distance):
                distance = potential

        position = (position + distance) % 28
        total += abs(distance) * step
    print("{0:.6f}".format(total / 15 + len(line)))
