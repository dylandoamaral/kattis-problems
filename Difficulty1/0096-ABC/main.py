import sys

numbers = sorted(map(int, sys.stdin.readline().strip().split()))
letters = sys.stdin.readline().strip()

hashFTW = dict()
alphabet = "ABC"

for i in range(0, len(numbers)):
    hashFTW[alphabet[i]] = numbers[i]

print(hashFTW[letters[0]], hashFTW[letters[1]], hashFTW[letters[2]])
