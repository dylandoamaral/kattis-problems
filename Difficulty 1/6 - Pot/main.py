#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())
total = 0

for i in range(0, n):
    a = sys.stdin.readline().strip()
    number = int(a[:-1])
    power = int(a[-1])
    total += number ** power

print(total)