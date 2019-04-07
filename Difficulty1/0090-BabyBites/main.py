#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip().split()

count = 1
for i in line:
    try:
        v = int(i)
        if v != count:
            break
        else:
            count += 1
    except:
        count += 1

if count - 1 == n:
    print("makes sense")
else:
    print("something is fishy")