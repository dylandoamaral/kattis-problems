#! /usr/bin/python3

import sys

(P, T) = map(int, sys.stdin.readline().strip().split())

answers = []
total = 0
for i in range(0, P):
    ok = True
    for j in range(0, T):
        answer = sys.stdin.readline().strip()
        answer = answer[1:]
        if answer != answer.lower():
            ok = False
    if ok:
        total += 1

print(total)