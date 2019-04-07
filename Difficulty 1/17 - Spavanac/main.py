#! /usr/bin/python3

import sys


time = sys.stdin.readline().strip().split()
hours = int(time[0])
minutes = int(time[1])

minutes -= 45
if minutes < 0:
    hours -= 1

print(hours % 24, ' ', minutes % 60)