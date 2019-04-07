#! /usr/bin/python3

import sys


def win(word, propositions):
    life = 10
    word = set(word)
    size = len(word)
    for letter in propositions:
        if letter not in word:
            life -= 1
        else:
            size -= 1
        if size == 0:
            break
    if life <= 0:
        return False
    return True


word = sys.stdin.readline().strip()
propositions = sys.stdin.readline().strip()

if win(word, propositions):
    print('WIN')
else:
    print('LOSE')