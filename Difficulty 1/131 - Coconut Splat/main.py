#! /usr/bin/python3

import sys
import math


def getPlayer(pos):
    return math.floor(pos / 2)


def getHand(pos):
    return pos % 2


def next(pos, players):
    if players[getPlayer(pos)][getHand(pos)] == "folded":
        pos += 2 - getHand(pos)
        pos = pos % (len(players) * 2)
    else:
        pos += 1
        pos = pos % (len(players) * 2)

    if players[getPlayer(pos)][getHand(pos)] == "back":
        while players[getPlayer(pos)][getHand(pos)] == "back":
            pos += 1
            pos = pos % (len(players) * 2)
    return pos


def countAlive(tab):
    count = 0
    for i in tab:
        if i[2]:
            count += 1
    return count


def getWinner(tab):
    player = 0
    for i in tab:
        player += 1
        if i[2]:
            return player


s, n = map(int, sys.stdin.readline().strip().split())

players = [["folded", "folded", True] for i in range(0, n)] # folded, fist, palm, back
pos = 0

while True:

    for i in range(0, s - 1):
        pos = next(pos, players)

    playerId = getPlayer(pos)
    handId = getHand(pos)

    if players[playerId][handId] == "folded":
        players[playerId][0] = "fist"
        players[playerId][1] = "fist"
        pos = pos - handId
    elif players[playerId][handId] == "fist":
        players[playerId][handId] = "palm"
        pos = next(pos, players)
    elif players[playerId][handId] == "palm":
        players[playerId][handId] = "back"
        if players[playerId][0] == "back" and players[playerId][1] == "back":
            players[playerId][2] = False
            if countAlive(players) == 1:
                break
        pos = next(pos, players)

print(getWinner(players))