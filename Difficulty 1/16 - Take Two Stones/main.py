#! /usr/bin/python3

import sys


N = int(sys.stdin.readline().strip())
if N % 2 == 0:
    print("Bob")
else:
    print("Alice")
