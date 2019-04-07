#! /usr/bin/python3

import sys

n = sys.stdin.readline().strip().split()
X, Y, N = int(n[0]),  int(n[1]),  int(n[2])

for i in range(1, N + 1):
    if i % X == 0 and i % Y == 0:
        print('Fizzbuzz')
    elif i % X == 0:
        print('Fizz')
    elif i % Y == 0:
        print('Buzz')
    else:
        print(i)
