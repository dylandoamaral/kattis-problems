#! /usr/bin/python3

import sys

patient = sys.stdin.readline().strip()
doctor = sys.stdin.readline().strip()

if len(patient) < len(doctor):
    print("no")
else:
    print("go")