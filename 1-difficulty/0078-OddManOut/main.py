#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())

case = 1

for i in range(0, n):
    n_guest = int(sys.stdin.readline().strip())
    guests = sys.stdin.readline().strip().split()
    for ask in range(0, len(guests)):
        if guests.count(guests[ask]) == 1:
            print("Case #", case, ": ", guests[ask], sep='')
            case += 1
            break
