#! /usr/bin/python3

import sys

starter = int(sys.stdin.readline().strip())
turn = int(sys.stdin.readline().strip())
timeglobal = 210
curr = starter

for i in range(0, turn):
    line = sys.stdin.readline().strip().split()
    timestamp = int(line[0])
    answer = line[1]
    timeglobal -= timestamp
    if timeglobal < 0:
        print(curr)
        break
    else:
        if answer == 'T':
            curr += 1
            if curr == 9:
                curr = 1