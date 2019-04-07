#! /usr/bin/python3

import sys


def rotation_value(word):
    total = 0
    for c in word:
        total += ord(c) - 65
    return total % 26


def rotation(word, n):
    result = ""
    for c in word:
        added_character = ord(c) + n
        if added_character > 90:
            added_character = added_character - 26
        result += chr(added_character)
    return result


line = sys.stdin.readline().strip()
length = len(line)

left = line[:int(length/2)]
right = line[int(length/2):]

rv_left = rotation_value(left)
rv_right = rotation_value(right)

r_left = rotation(left, rv_left)
r_right = rotation(right, rv_right)

result = ""
for i in range(0, int(length/2)):
    n = ord(r_right[i]) - ord('A')
    added_character = ord(r_left[i]) + n
    if added_character > 90:
        added_character = added_character - 26
    result += chr(added_character)
print(result)