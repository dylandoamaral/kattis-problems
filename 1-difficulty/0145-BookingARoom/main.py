#! /usr/bin/python3

import sys

(nRooms, bRooms) = map(int, sys.stdin.readline().strip().split())

booked = []

for room in range(bRooms):
    booked.append(int(sys.stdin.readline().strip()))

if len(booked) == nRooms:
    print("too late")
else:
    i = 1
    while i in booked:
        i += 1
    print(i)