#! /usr/bin/python3

import sys

n = sys.stdin.readline().strip()

previous = '?'
hissing = 'no hiss'
for i in n:
    if previous == 's' and i == 's':
        hissing = 'hiss'
    previous = i

print(hissing)