#! /usr/bin/python3

import sys

(a1, c1, a2, c2) = map(int, sys.stdin.readline().strip().split())
people = list(map(int, sys.stdin.readline().strip().split()))
status = ["none", "none", "none"]

(curr1, type1) = (0, "aggressif")
(curr2, type2) = (0, "aggressif")

passed = 0

for i in range(0, max(people) + 1):
    for index in range(len(people)):
        if i == people[index]:
            passed = 0
            if type1 == "calm":
                passed += 1
            if type2 == "calm":
                passed += 1

            if passed == 0:
                status[index] = "both"
            elif passed == 1:
                status[index] = "one"
            elif passed == 2:
                status[index] = "none"

    if type1 == "calm" and curr1 == c1:
        type1 = "aggressif"
        curr1 = 0
    elif type1 == "aggressif" and curr1 == a1:
        type1 = "calm"
        curr1 = 0

    if type2 == "calm" and curr2 == c2:
        type2 = "aggressif"
        curr2 = 0
    elif type2 == "aggressif" and curr2 == a2:
        type2 = "calm"
        curr2 = 0

    curr1 += 1
    curr2 += 1

for statu in status:
    print(statu)