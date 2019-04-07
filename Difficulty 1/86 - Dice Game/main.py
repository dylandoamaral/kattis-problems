#! /usr/bin/python3

import sys


def esperance(a, b):
    total = 0
    for i in range(a, b + 1):
        total += i
    return total * 1 / (b - a + 1)


dicesGunnar = sys.stdin.readline().strip().split()
dicesEmma = sys.stdin.readline().strip().split()

a1G, b1G, a2G, b2G = int(dicesGunnar[0]), int(dicesGunnar[1]), int(dicesGunnar[2]), int(dicesGunnar[3])
a1E, b1E, a2E, b2E = int(dicesEmma[0]), int(dicesEmma[1]), int(dicesEmma[2]), int(dicesEmma[3])

EGunnar = esperance(a1G + a2G, b1G + b2G)
EEmma = esperance(a1E + a2E, b1E + b2E)

if EGunnar > EEmma:
    print("Gunnar")
elif EGunnar < EEmma:
    print("Emma")
else:
    print("Tie")