#! /usr/bin/python3

import sys, time


def findInter(a, b):
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if a[i] == b[j]:
                return i, j


a, b = sys.stdin.readline().strip().split()
x, y = findInter(a, b)
word = ""

for i in range(0, len(b)):
    if i == y:
        print(a)
    else:
        for j in range(0, len(a)):
            if j == x:
                print(b[i], end="")
            else:
                print('_', end="", flush=True)
        print("")