#! /usr/bin/python3

import sys


def encode(word):
    word += "*"
    output = ""
    last = None
    counter = 0

    for letter in word:
        if last and letter != last:
            output += last
            output += str(counter)
            counter = 1
        else:
            counter += 1
        last = letter
    return output


def decode(word):
    output = ""
    for i in range(0, len(word), 2):
        l, n = word[i], int(word[i + 1])
        for j in range(0, n):
            output += l
    return output


line = sys.stdin.readline().strip().split()
state = line[0]
word = line[1]

if state == 'E':
    print(encode(word))
else:
    print(decode(word))
