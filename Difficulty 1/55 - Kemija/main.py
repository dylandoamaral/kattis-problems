#! /usr/bin/python3

import sys

lines = sys.stdin.readline().strip()

vowel = ['a', 'e', 'i', 'o', 'u']
response = ""
ignore = 0

for i in range(0, len(lines)):
    ignore -= 1
    if ignore > 0:
        continue
    response += lines[i]
    if i + 2 < len(lines) and lines[i] in vowel and lines[i] == lines[i + 2] and lines[i + 1] == 'p':
        ignore = 3

print(response)