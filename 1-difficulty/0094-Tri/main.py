#! /usr/bin/python3

import sys

line = sys.stdin.readline().strip().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])

if a + b == c:
    print(a, "+", b, "=", c, sep="")
elif a == b + c:
    print(a, "=", b, "+", c, sep="")
elif a - b == c:
    print(a, "-", b, "=", c, sep="")
elif a == b - c:
    print(a, "=", b, "-", c, sep="")
elif a * b == c:
    print(a, "*", b, "=", c, sep="")
elif a == b * c:
    print(a, "=", b, "*", c, sep="")
elif b != 0 and a / b == c:
    print(a, "/", b, "=", c, sep="")
elif c != 0 and a == b / c:
    print(a, "=", b, "/", c, sep="")