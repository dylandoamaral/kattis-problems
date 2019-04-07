#! /usr/bin/python3

import sys

i = 0
while True:
    i += 1
    line = list(map(int, sys.stdin.readline().strip().split()))[1:]
    if line == 'EOF' or len(line) == 0 or line == '':
        break;
    minima = min(line)
    maxima = max(line)
    ranger = maxima - minima
    print("Case " + str(i) + ": " + str(minima) + " " + str(maxima) + " " + str(ranger))