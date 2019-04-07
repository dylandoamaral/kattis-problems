#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())
winners = []
schools = []
prizes = 12
for i in range(0, n):
    if prizes == 0:
        break;
    team = sys.stdin.readline().strip()
    school = team.split()[0]
    if school not in schools:
        winners.append(team)
        schools.append(school)
        prizes -= 1
for winner in winners:
    print(winner)