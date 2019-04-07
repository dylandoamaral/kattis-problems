#! /usr/bin/python3

import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))
res = abs(N - M)
if N < M:
    if res == 1:
        print("Dr. Chaz will have", res, "piece of chicken left over!")
    else:
        print("Dr. Chaz will have", res, "pieces of chicken left over!")
else:
    if res == 1:
        print("Dr. Chaz needs", res, "more piece of chicken!")
    else:
        print("Dr. Chaz needs", res, "more pieces of chicken!")
