#! /usr/bin/python3

import sys
import math

def findXY(number, order):
    y = 0
    for line in order:
        x = 0
        for digit in line:
            if digit == number:
                return (x, y)
            x += 1
        y += 1


def getDistance(number, order):
    curr = number
    next = number + 1
    currPos = findXY(curr, order)
    nextPos = findXY(next, order)

    if currPos[0] == nextPos[0]:
        return abs(currPos[1] - nextPos[1])
    elif currPos[1] == nextPos[1]:
        return abs(currPos[0] - nextPos[0])
    else:
        return math.sqrt((currPos[1] - nextPos[1])**2 + (currPos[0] - nextPos[0])**2)

order = []
order.append(list(map(int, sys.stdin.readline().strip().split())))
order.append(list(map(int, sys.stdin.readline().strip().split())))
order.append(list(map(int, sys.stdin.readline().strip().split())))

distance = 0
for number in range(1, 9):
    distance += getDistance(number, order)

print(distance)