#! /usr/bin/python3

import sys

info = list(map(int, sys.stdin.readline().strip().split()))
processes = list(map(int, sys.stdin.readline().strip().split()))

total = 0
done = 0

for i in range(0, len(processes)):
    if total + processes[i] > info[1]:
        break
    total += processes[i]
    done += 1

print(done)

