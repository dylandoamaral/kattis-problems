#! /usr/bin/python3

import sys

pieces = [1, 1, 2, 2, 2, 8]
nums = sys.stdin.readline().strip().split()
for i in range(0,len(pieces)):
    res = pieces[i] - int(nums[i])
    print(res, " ", end='')
