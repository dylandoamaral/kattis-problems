#! /usr/bin/python3

import sys


n = int(sys.stdin.readline())

for sample in range(0, n):

    line = sys.stdin.readline().strip().split()
    num = int(line[0])
    comps = line[1].split("/")

    n = 0
    (p, q) = (int(comps[0]), int(comps[1]))

    steps = []
    i = 0
    while True:
        if p == 1 and q == 1:
            i += 1
            break
        pNext = p
        qNext = q
        if min([pNext, qNext]) == pNext:
            p = pNext
            q = qNext - p
            steps.append("l")
        else:
            q = qNext
            p = pNext - q
            steps.append("r")
        i += 1
    k = 0
    for step in steps[::-1]:
        if step == "l":
            k = 2 * k + 1
        else:
            k = 2 * k + 2
    print(num, k + 1)