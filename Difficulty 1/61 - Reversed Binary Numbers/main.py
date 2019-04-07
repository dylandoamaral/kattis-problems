#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())
n_binary = bin(n)[2:]
n_binary = n_binary[::-1]
print(int(n_binary, 2))
