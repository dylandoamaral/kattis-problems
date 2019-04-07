#! /usr/bin/python3

import sys


def map(letter):
    if ord(letter) == ord("_"):
        return 26
    elif ord(letter) == ord("."):
        return 27
    else:
        return ord(letter) - ord("A")


def demap(num):
    if num == 26:
        return "_"
    elif num == 27:
        return "."
    else:
        return chr(num + ord("A"))


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."


while True:
    line = sys.stdin.readline().strip().split()
    if line[0] == "0":
        break;
    rot = int(line[0])
    line = line[1][::-1]
    code = ""
    for letter in line:
        tmp = (map(letter) + rot) % len(alphabet)
        code += demap(tmp)
    print(code)