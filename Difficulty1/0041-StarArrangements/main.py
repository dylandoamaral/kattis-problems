#! /usr/bin/python3

import sys

def checkifitwork(r_1, r_2, total):
    result = 0
    while True:
        result += r_1
        if result == total:
            return True
        result += r_2
        if result == total:
            return True
        if result > total:
            return False


n = int(sys.stdin.readline().strip())
print(n, ":", sep='')

max_one_row = int(n / 2) + 1
possibilities = []

for i in range(max_one_row, 1, -1):
    r_1 = i
    r_2 = i
    if checkifitwork(r_1, r_2, n):
        possibilities.append((r_1, r_2))
    r_2 = i - 1
    if checkifitwork(r_1, r_2, n):
        possibilities.append((r_1, r_2))

for i in reversed(possibilities):
    print(i[0], ",", i[1], sep='')