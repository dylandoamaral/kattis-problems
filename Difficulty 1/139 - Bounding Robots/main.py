#! /usr/bin/python3

import sys


def bound(coord, size):
    if coord > size:
        return size
    elif coord < 0:
        return 0
    else:
        return coord


while True:
    (w, l) = map(int, sys.stdin.readline().strip().split())
    if w == 0 and l == 0:
        break;
    (w, l) = (w - 1, l - 1)
    n = int(sys.stdin.readline().strip())
    moves = []
    (x, y) = (0, 0) #robot
    (xt, yt) = (0, 0) #real
    for i in range(0, n):
        (direct, amount) = sys.stdin.readline().strip().split()
        (direct, amount) = (direct, int(amount))
        if direct == "u":
            (x, y) = (x, y + amount)
            (xt, yt) = (xt, yt + amount)
            (xt, yt) = (xt, bound(yt, l))
        elif direct == "d":
            (x, y) = (x, y - amount)
            (xt, yt) = (xt, yt - amount)
            (xt, yt) = (xt, bound(yt, l))
        elif direct == "l":
            (x, y) = (x - amount, y)
            (xt, yt) = (xt - amount, yt)
            (xt, yt) = (bound(xt, w), yt)
        elif direct == "r":
            (x, y) = (x + amount, y)
            (xt, yt) = (xt + amount, yt)
            (xt, yt) = (bound(xt, w), yt)
    print("Robot thinks", x, y)
    print("Actually at", xt, yt)