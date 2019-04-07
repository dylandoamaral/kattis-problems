#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())
for i in range(0, n):
    numbers = sys.stdin.readline().strip()[::-1]
    total = 0
    for j in range(0, len(numbers)):
        if j % 2 == 1:
            tmp = int(numbers[j]) * 2
            while tmp >= 10:
                tmp = str(tmp)
                new = 0
                for number in tmp:
                    new += int(number)
                tmp = new
            total += tmp
        else:
            total += int(numbers[j])
    if total % 10 == 0:
        print("PASS")
    else:
        print("FAIL")