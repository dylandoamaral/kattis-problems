#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())


for i in range(0, n):
    s = sys.stdin.readline().strip().split()
    name = s[0]
    yearStudy = int(s[1].split('/')[0])
    yearBirth = int(s[2].split('/')[0])
    courses = int(s[3])
    if yearStudy >= 2010:
        print(name, "eligible")
    elif yearBirth >= 1991:
        print(name, "eligible")
    else:
        if courses <= 40:
            print(name, "coach petitions")
        else:
            print(name, "ineligible")
