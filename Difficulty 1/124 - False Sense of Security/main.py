#! /usr/bin/python3

import sys
from collections import deque

def toMorse(word):
    morsed = ""
    lengths = []
    for letter in word:
        morsed += codex[letter]
        lengths.append(len(codex[letter]))
    return morsed, lengths


codex = dict()
decodex = dict()
codex["A"] = ".-"
codex["B"] = "-..."
codex["C"] = "-.-."
codex["D"] = "-.."
codex["E"] = "."
codex["F"] = "..-."
codex["G"] = "--."
codex["H"] = "...."
codex["I"] = ".."
codex["J"] = ".---"
codex["K"] = "-.-"
codex["L"] = ".-.."
codex["M"] = "--"
codex["N"] = "-."
codex["O"] = "---"
codex["P"] = ".--."
codex["Q"] = "--.-"
codex["R"] = ".-."
codex["S"] = "..."
codex["T"] = "-"
codex["U"] = "..-"
codex["V"] = "...-"
codex["W"] = ".--"
codex["X"] = "-..-"
codex["Y"] = "-.--"
codex["Z"] = "--.."
codex["_"] = "..--"
codex[","] = ".-.-"
codex["."] = "---."
codex["?"] = "----"

decodex[".-"] = "A"
decodex["-..."] = "B"
decodex["-.-."] = "C"
decodex["-.."] = "D"
decodex["."] = "E"
decodex["..-."] = "F"
decodex["--."] = "G"
decodex["...."] = "H"
decodex[".."] = "I"
decodex[".---"] = "J"
decodex["-.-"] = "K"
decodex[".-.."] = "L"
decodex["--"] = "M"
decodex["-."] = "N"
decodex["---"] = "O"
decodex[".--."] = "P"
decodex["--.-"] = "Q"
decodex[".-."] = "R"
decodex["..."] = "S"
decodex["-"] = "T"
decodex["..-"] = "U"
decodex["...-"] = "V"
decodex[".--"] = "W"
decodex["-..-"] = "X"
decodex["-.--"] = "Y"
decodex["--.."] = "Z"
decodex["..--"] = "_"
decodex[".-.-"] = ","
decodex["---."] = "."
decodex["----"] = "?"

word = sys.stdin.readline().strip()
while word:
    crypted, lengths = toMorse(word)
    lengths = lengths[::-1]
    morse = ""
    i = 0
    message = ""
    for letter in crypted:
        morse += letter
        if len(morse) == lengths[i]:
            message += decodex[morse]
            i += 1
            morse = ""
    print(message)
    word = sys.stdin.readline().strip()
