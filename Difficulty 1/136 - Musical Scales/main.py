#! /usr/bin/python3

import sys


def getScale(note, notes, tones):
    major = [note]
    index = notes.index(note)
    for tone in tones:
        index += tone
        major.append(notes[index % len(notes)])
    return major


def isItOk(notes, scale):
    for note in notes:
        if note not in scale:
            return False
    return True


notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
tones = [2, 2, 1, 2, 2, 2, 1]
scales = [getScale(note, notes, tones) for note in notes]

sys.stdin.readline()
readed = set(sys.stdin.readline().strip().split())

works = []
for scale in scales:
    if(isItOk(readed, scale)):
        works.append(scale[0])

if len(works) == 0:
    print("none")
else:
    for work in works:
        print(work, "", end = "")