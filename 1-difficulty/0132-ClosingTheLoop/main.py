#! /usr/bin/python3

import sys


n = int(sys.stdin.readline())

for i in range(0, n):
    int(sys.stdin.readline())
    segments = (sys.stdin.readline().strip().split())
    blues = []
    reds = []
    for segment in segments:
        if segment[-1] == "B":
            blues.append(int(segment[:-1]))
        else:
            reds.append(int(segment[:-1]))
    blues.sort()
    reds.sort()
    blues = blues[::-1]
    reds = reds[::-1]
    minima = min(len(blues), len(reds))
    length = 0
    for j in range(0, minima):
        length += blues[j] + reds[j]
    print("Case #", i + 1, ": ", sep="", end="")
    if minima == 0:
        print(0)
    else:
        print(length - (2 * minima))