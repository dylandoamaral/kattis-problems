#! /usr/bin/python3

import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    l1 = []
    l2 = []
    for i in range(0, n):
        l1.append(int(sys.stdin.readline()))
    for i in range(0, n):
        l2.append(int(sys.stdin.readline()))

    l1sort = l1.copy()
    l1sort.sort()
    l2sort = l2.copy()
    l2sort.sort()

    mydict = dict()

    for element in range(0, n):
        mydict[l1sort[element]] = l2sort[element]

    for element in l1:
        print(mydict[element])
    print("")