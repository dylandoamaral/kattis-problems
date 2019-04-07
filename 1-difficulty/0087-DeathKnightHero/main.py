#! /usr/bin/python3

import sys


def nomistake(attacks):
    last = "Z"
    for attack in attacks:
        if attack == "D" and last == "C":
            return False
        last = attack
    return True


n = int(sys.stdin.readline().strip())
total = 0

for battle in range(0, n):
    attacks = sys.stdin.readline().strip()
    if(nomistake(attacks)):
        total += 1

print(total)