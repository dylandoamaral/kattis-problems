#! /usr/bin/python3

import sys


def PGCD(A, B):
    C = A % B
    while C != 0:
        A = B
        B = C
        C = A % B
    return B


n = int(sys.stdin.readline().strip())
radius = list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, len(radius)):
    print(str(round(radius[0] / PGCD(radius[0], radius[i]))) + "/" + str(round(radius[i] / PGCD(radius[0], radius[i]))))