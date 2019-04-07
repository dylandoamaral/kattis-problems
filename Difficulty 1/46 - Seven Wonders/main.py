#! /usr/bin/python3

import sys

line = sys.stdin.readline().strip()

cards = [0, 0, 0]

for card in line:
    if card == "T":
        cards[0] += 1
    elif card == "C":
        cards[1] += 1
    else:
        cards[2] += 1

total = cards[0] ** 2 + cards[1] ** 2 + cards[2] ** 2 + min(cards) * 7
print(total)