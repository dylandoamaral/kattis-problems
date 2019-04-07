#! /usr/bin/python3

import sys

problems = dict()
count = 0

while True:
    n = int(sys.stdin.readline().strip())
    count += 1
    animals = dict()
    if n == 0:
        break;
    for i in range(0, n):
        line = sys.stdin.readline().strip().split()
        animal = line[-1].lower()
        if animal in animals.keys():
            animals[animal] += 1
        else:
            animals[animal] = 1
    print("List " + str(count) + ":")
    for key, value in sorted(animals.items()):
        print(key, "|", value)


