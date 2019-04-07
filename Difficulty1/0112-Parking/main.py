#! /usr/bin/python3

import sys


def isParked(truck, min):
    if truck[0] <= min < truck[1]:
        return True
    return False


prices = list(map(int, sys.stdin.readline().strip().split()))

trucks = []
low, high = 101, -1
total = 0

for i in range(0, 3):
    times = list(map(int, sys.stdin.readline().strip().split()))
    trucks.append(times)
    if times[0] < low:
        low = times[0]
    if times[1] > high:
        high = times[1]

for i in range(low, high + 1):
    truckParked = 0
    for j in range (0, 3):
        if isParked(trucks[j], i):
            truckParked += 1
    total += prices[truckParked - 1] * truckParked

print(total)