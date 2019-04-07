#! /usr/bin/python3

import sys


megabytes = int(sys.stdin.readline().strip())
months = int(sys.stdin.readline().strip())

available = megabytes
for i in range(0,months):
    spend = int(sys.stdin.readline().strip())
    available += megabytes - spend

print(available)
