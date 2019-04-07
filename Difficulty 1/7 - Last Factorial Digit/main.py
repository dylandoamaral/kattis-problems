#! /usr/bin/python3

import sys


def factorial(n):
    if n == 1 or n == 0:
        return(1)
    return n * factorial(n - 1)


n = int(sys.stdin.readline().strip())
total = 0

for i in range(0, n):
    a = int(sys.stdin.readline().strip())
    a = factorial(a)
    print(a % 10)
