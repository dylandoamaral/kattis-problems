#! /usr/bin/python3

import sys

problems = dict()

while True:
    line = sys.stdin.readline().strip().split()
    if line[0] == "-1":
        break;
    minutes = int(line[0])
    problem = line[1]
    state = line[2]
    if problem not in problems.keys():
        problems[problem] = {
            "minutes": 0,
            "state": "wrong"
        }
    problems[problem]["state"] = state
    if problems[problem]["state"] == "right":
        problems[problem]["minutes"] += minutes
    else:
        problems[problem]["minutes"] += 20


solved = 0
minutes = 0

for key, value in problems.items():
    if value["state"] == "right":
        solved += 1
        minutes += value["minutes"]

print(solved, minutes)