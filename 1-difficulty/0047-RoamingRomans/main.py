#! /usr/bin/python3

import sys

miles = float(sys.stdin.readline().strip())
print(round(miles*1000*(5280/4854)))