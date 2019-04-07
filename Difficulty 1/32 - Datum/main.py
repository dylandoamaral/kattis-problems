#! /usr/bin/python3

import sys

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
shift = 3
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

n = sys.stdin.readline().strip().split()
day = int(n[0])
month = int(n[1])

total = 0
for i in range(0, month - 1):
    total += months[i]

total += day
print(days[(total + shift - 1) % 7])