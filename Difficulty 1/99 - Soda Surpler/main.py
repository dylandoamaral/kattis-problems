#! /usr/bin/python3

import sys
import math

soda = list(map(int, sys.stdin.readline().strip().split()))

drinked = 0
empty = soda[0] + soda[1]

while empty >= soda[2]:
    drink = math.trunc(empty / soda[2])
    empty -= drink * soda[2]
    drinked += drink
    empty += drink

print(drinked)