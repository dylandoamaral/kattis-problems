#! /usr/bin/python3

import sys


def isharshard(n):
    n_string = str(n)
    total = 0
    for num in n_string:
        total += int(num)
    if n%total == 0:
        return True
    return False


n = int(sys.stdin.readline().strip())

while isharshard(n) is False:
    n += 1

print(n)

