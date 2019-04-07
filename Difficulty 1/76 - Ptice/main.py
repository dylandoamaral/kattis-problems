#! /usr/bin/python3

import sys


def best(dictionary):
    bests = []
    score = -1
    for key, values in dictionary.items():
        if values["score"] > score:
            score = values["score"]
            bests = []
            bests.append((key, values["score"]))
        elif values["score"] == score:
            bests.append((key, score))
    return bests


n = int(sys.stdin.readline().strip())
answers = sys.stdin.readline().strip()

participant = dict()
participant['Adrian'] = {
    "sequence": "ABC",
    "score": 0
}

participant['Bruno'] = {
    "sequence": "BABC",
    "score": 0
}

participant['Goran'] = {
    "sequence": "CCAABB",
    "score": 0
}

index = 0
for letter in answers:
    for key, values in participant.items():
        if values["sequence"][index % len(values["sequence"])] == letter:
            values["score"] += 1
    index += 1

bests = best(participant)
print(bests[0][1])
for best in bests:
    print(best[0])