#! /usr/bin/python3

import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'

lena, lenb = list(map(int, sys.stdin.readline().strip().split()))
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

k = ""
first = ord('a')

caesar = ord(a[-1]) - ord(b[-1])

res = ""
for letter in b:
    res += chr(first + (ord(letter) - first + caesar) % 26)

print(res)