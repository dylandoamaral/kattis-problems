#! /usr/bin/python3

import sys

line = sys.stdin.readline()
line = line.strip().split()
contestant = int(line[0])
solved = int(line[1])
for i in range(0, contestant):
    line = sys.stdin.readline()
print(solved)