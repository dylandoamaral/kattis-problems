#! /usr/bin/python3

import sys


def find(money, dictionary):
    best = 0, {"costs": 0, "value": 0}
    for k, v in dictionary.items():
        if money >= v["costs"] and v["value"] > best[1]["value"]:
            best = (k, v)
    return best


line = sys.stdin.readline().strip().split()
G = int(line[0])
S = int(line[1])
C = int(line[2])

victoryCards = dict()
victoryCards['Province'] = {"costs": 8, "value": 6}
victoryCards['Duchy'] = {"costs": 5, "value": 3}
victoryCards['Estate'] = {"costs": 2, "value": 1}

treasuresCards = dict()
treasuresCards['Gold'] = {"costs": 6, "value": 3}
treasuresCards['Silver'] = {"costs": 3, "value": 2}
treasuresCards['Copper'] = {"costs": 0, "value": 1}

buying_power = G * 3 + S * 2 + C * 1

victory = find(buying_power, victoryCards)
treasure = find(buying_power, treasuresCards)

if victory[0] == 0:
    print(treasure[0])
else:
    print(victory[0], "or", treasure[0])

