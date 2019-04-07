#! /usr/bin/python3

import sys

n = sys.stdin.readline().strip().split()

n_set = set(n)

if len(n) == len(n_set):
    print("yes")
else:
    print("no")
