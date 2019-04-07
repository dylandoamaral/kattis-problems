#! /usr/bin/python3

import sys

nums = sys.stdin.readline().strip().split("-")
res = ""
for i in nums:
    res += i[0]
print(res)