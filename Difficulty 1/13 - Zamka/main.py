#! /usr/bin/python3

import sys


def sum_digits(n):
    total = 0
    for i in str(n):
        total += int(i)
    return total


def find_minimal(L, D, X):
    for i in range(L, D + 1):
        if sum_digits(i) == X:
            return i


def find_maximal(L, D, X):
    for i in range(D, L - 1, -1):
        if sum_digits(i) == X:
            return i


L = int(sys.stdin.readline().strip())
D = int(sys.stdin.readline().strip())
X = int(sys.stdin.readline().strip())

print(find_minimal(L, D, X))
print(find_maximal(L, D, X))





