#! /usr/bin/python3

import sys


def everything(tab):
    tmp = str(tab)
    for i in tmp:
        if tmp.count(i) != 1 or int(i) == 0 or tab % int(i) != 0:
            return False
    return True


line = sys.stdin.readline().strip().split()
a = int(line[0])
b = int(line[1])

possibility = 0
for i in range(a, b + 1):
    if everything(i):
        possibility += 1
print(possibility)
