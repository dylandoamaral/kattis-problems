#! /usr/bin/python3

import sys


def problem(sequence):
    for element in sequence:
        if element is None:
            return True
    return False


def convert(sequence, numbers):
    for key, value in numbers.items():
        if value == sequence:
            return key
    return None

numbers = dict()
numbers[0] = ['***', '* *', '* *', '* *', '***']
numbers[1] = ['  *', '  *', '  *', '  *', '  *']
numbers[2] = ['***', '  *', '***', '*  ', '***']
numbers[3] = ['***', '  *', '***', '  *', '***']
numbers[4] = ['* *', '* *', '***', '  *', '  *']
numbers[5] = ['***', '*  ', '***', '  *', '***']
numbers[6] = ['***', '*  ', '***', '* *', '***']
numbers[7] = ['***', '  *', '  *', '  *', '  *']
numbers[8] = ['***', '* *', '***', '* *', '***']
numbers[9] = ['***', '* *', '***', '  *', '***']

code = []
transcript = []

for i in range(0, 5):
    code.append(sys.stdin.readline()[:-1])

digits = (1 + len(code[0]))/4

for i in range(0, int(digits)):
    number = []
    for line in code:
        line = list(line)
        txt = ""
        for char in range(i * 4, (i * 4) + 3):
            txt += line[char]
        number.append(txt)
    transcript.append(convert(number, numbers))

if problem(transcript):
    print("BOOM!!")
else:
    transcript = int(''.join(map(str, transcript)))
    if transcript % 6 == 0:
        print("BEER!!")
    else:
        print("BOOM!!")