#! /usr/bin/python3

import sys

cards = dict()
cards['A'] = dict({
    "dominant": 11,
    "non dominant": 11
})
cards['K'] = dict({
    "dominant": 4,
    "non dominant": 4
})
cards['Q'] = dict({
    "dominant": 3,
    "non dominant": 3
})
cards['J'] = dict({
    "dominant": 20,
    "non dominant": 2
})
cards['T'] = dict({
    "dominant": 10,
    "non dominant": 10
})
cards['9'] = dict({
    "dominant": 14,
    "non dominant": 0
})
cards['8'] = dict({
    "dominant": 0,
    "non dominant": 0
})
cards['7'] = dict({
    "dominant": 0,
    "non dominant": 0
})

line = sys.stdin.readline().strip().split()
n = int(line[0])
dominant = line[1]

total = 0

for i in range(0, 4* n):
    line = sys.stdin.readline().strip()
    if line[1] == dominant:
        total += cards[line[0]]["dominant"]
    else:
        total += cards[line[0]]["non dominant"]

print(total)