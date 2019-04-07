#! /usr/bin/python3

import sys

amount = list(map(int, sys.stdin.readline().strip().split()))
ratio = list(map(int, sys.stdin.readline().strip().split()))

fusion = [amount[0] / ratio[0], amount[1] / ratio[1], amount[2] / ratio[2]]
max = min(fusion)

print("{0:.4f}".format(amount[0] - ratio[0] * max), "{0:.4f}".format(amount[1] - ratio[1] * max), "{0:.4f}".format(amount[2] - ratio[2] * max))