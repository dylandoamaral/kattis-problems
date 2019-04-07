#! /usr/bin/python3

import sys

while True:
    x, y = list(map(int, sys.stdin.readline().strip().split()))
    if x == 0 and y == 0:
        break;
    if x + y == 13:
        print("Never speak again.")
    elif x < y:
        print("Left beehind.")
    elif x > y:
        print("To the convention.")
    else:
        print("Undecided.")