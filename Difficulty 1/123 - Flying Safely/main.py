#! /usr/bin/python3

import sys
from collections import deque

n = int(sys.stdin.readline().strip())

for i in range(0, n):
    n, m = map(int,sys.stdin.readline().strip().split())
    graph = dict()
    for j in range(0, m):
        a, b = map(int,sys.stdin.readline().strip().split())
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = list([b])
        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = list([a])
    curr = min(graph.items(), key=lambda x: len(x[1]))
    marqued = [0 for y in range(0, n + 1)]
    queue = deque([curr[0]])
    marqued[curr[0]] = 1
    count = 0
    while len(queue) != 0:
        s = queue.popleft()
        count += 1
        for node in graph[s]:
            if marqued[node] == 0:
                queue.append(node)
                marqued[node] = 1
    print(count - 1)