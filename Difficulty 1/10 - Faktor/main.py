#! /usr/bin/python3

import sys

nums = sys.stdin.readline().strip().split()
a = int(nums[0])
b = int(nums[1])
print(a * (b - 1) + 1)