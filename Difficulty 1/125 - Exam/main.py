#! /usr/bin/python3

import sys

n = int(sys.stdin.readline().strip())
me = list(sys.stdin.readline().strip())
him = list(sys.stdin.readline().strip())

simi = 0

for i in range(0, len(me)):
    if me[i] == him[i]:
        simi += 1

reste = len(me) - n
diff = len(me) - simi

print(min(n, simi) + min(diff, reste))
