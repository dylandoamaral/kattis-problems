#! /usr/bin/python3

import sys

line = list(map(int, sys.stdin.readline().strip().split()))
bob_year = line[0]
bob_retire = line[1]
bob_save = line[2]
alice_year = line[3]
alice_save = line[4]

bob_gain = (bob_retire - bob_year) * bob_save

alice_gain = 0
alice_retire = alice_year
while alice_gain <= bob_gain:
    alice_gain += alice_save
    alice_retire += 1

print(alice_retire)