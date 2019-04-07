#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())

befDel = sys.stdin.readline().strip()
aftDel = sys.stdin.readline().strip()

length = len(befDel)
control = True

for i in range(0, length):
    if int(befDel[i]) != (int(aftDel[i]) + (n % 2)) % 2:
        control = False
        break;

if control:
    print("Deletion succeeded")
else:
    print("Deletion failed")
