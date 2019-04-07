#! /usr/bin/python3

import sys
from collections import deque


def fight(head, tail):
    current = deque([(head, tail)])
    next = deque([])

    marqued = [[0 for x in range(200)] for y in range(200)]
    turn = 0

    while True:
        while len(current) > 0:
            curr = current.popleft()
            if curr[0] == 0 and curr[1] == 0:
                return turn
            if curr[1] + 1 <= 100 and curr[1] - 1 >= 0 and marqued[curr[0]][curr[1] + 1] == 0:
                next.append((curr[0], curr[1] + 1))
                marqued[curr[0]][curr[1] + 1] = 1
            if curr[0] - 2 >= 0 and marqued[curr[0] - 2][curr[1]] == 0:
                next.append((curr[0] - 2, curr[1]))
                marqued[curr[0] - 2][curr[1]] = 1
            if curr[0] + 1 <= 100 and curr[1] - 2 >= 0 and marqued[curr[0] + 1][curr[1] - 2] == 0:
                next.append((curr[0] + 1, curr[1] - 2))
                marqued[curr[0] + 1][curr[1] - 2] = 1
        turn += 1
        current = next.copy()
        next.clear()
        if len(current) == 0:
            return -1

line = sys.stdin.readline().strip().split()
head = int(line[0])
tail = int(line[1])

while head != 0 or tail != 0:
    print(fight(head, tail))
    line = sys.stdin.readline().strip().split()
    head = int(line[0])
    tail = int(line[1])