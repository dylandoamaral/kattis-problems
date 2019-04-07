#! /usr/bin/python3

import sys


def printSequence(sequence):
    for element in sequence:
        print(element, end=" ")


sequence = list(map(int, sys.stdin.readline().strip().split()))


while sequence != [1, 2, 3, 4, 5]:
    for i in range(0, 4):
        if sequence[i] > sequence[i + 1]:
            tmp = sequence[i]
            sequence[i] = sequence[i + 1]
            sequence[i + 1] = tmp
            printSequence(sequence)
            print()

