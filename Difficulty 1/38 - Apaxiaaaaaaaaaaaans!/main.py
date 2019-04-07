#! /usr/bin/python3

import sys

n = sys.stdin.readline().strip()
output = ""
previous = "?"

for i in n:
    if previous == i:
        continue
    output += i
    previous = i

print(output)