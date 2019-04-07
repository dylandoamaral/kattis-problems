#! /usr/bin/python3

import sys

nums = sys.stdin.readline().strip().split()
a = int(nums[0][::-1])
b = int(nums[1][::-1])

if a > b:
    print(a)
else:
    print(b)