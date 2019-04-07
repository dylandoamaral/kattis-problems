#! /usr/bin/python3

import sys

lines = sys.stdin.readline().strip().split()

if int(lines[0]) == 0 and int(lines[1]) == 0:
    print('Not a moose')
elif int(lines[0]) == int(lines[1]):
    print('Even', int(lines[0]) * 2)
else:
    print('Odd', max(int(lines[0]), int(lines[1])) * 2)