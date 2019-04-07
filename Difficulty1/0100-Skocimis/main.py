#! /usr/bin/python3

import sys

kangoo = sorted(map(int, sys.stdin.readline().strip().split()))

move = 0

while kangoo[0] != kangoo[1] - 1 or kangoo[1] != kangoo[2] - 1:
    left = False
    right = False
    if kangoo[0] < kangoo[1] - 1:
        left = True
    if kangoo[1] < kangoo[2] - 1:
        right = True

    if left and right:
        if kangoo[1] - kangoo[0] > kangoo[2] - kangoo[1]:
            kangoo[2] = kangoo[1] - 1
        else:
            kangoo[0] = kangoo[2] - 1
    else:
        if left:
            kangoo[2] = kangoo[1] - 1
        else:
            kangoo[0] = kangoo[2] - 1

    kangoo = sorted(kangoo)
    move += 1
print(move)
