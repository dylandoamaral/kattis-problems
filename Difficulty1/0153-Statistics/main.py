#! /usr/bin/python3

import sys


def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r


n = int(sys.stdin.readline().strip())

done = [-1 for i in range(0, 100001)]

for i in range(n):
    number = int(sys.stdin.readline().strip())
    if done[number] != -1:
        print(done[number])
    else:
        sumTotal = sum_digits3(number)
        for num in range(0, number)[::-1]:
            sumDigit = sum_digits3(num)
            if sumDigit == sumTotal - 1:
                done[number] = num
                break;
        print(num)