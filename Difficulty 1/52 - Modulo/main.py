#! /usr/bin/python3

import sys

numbers = []
for i in range(0, 10):
    n = int(sys.stdin.readline().strip())
    numbers.append(n % 42)

print(len(set(numbers)))