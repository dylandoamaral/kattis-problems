#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())

c = n ** (1/2)

print("{0:.5f}".format(4 * c))