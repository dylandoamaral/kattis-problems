import sys

n = int(sys.stdin.readline())
index = 1
while n != 0:
    names = []

    left = []
    right = []

    for i in range(0, n):
        names.append(sys.stdin.readline().strip())
    for i in range(0, n):
        if i % 2 == 1:
            right.append(names[i])
        else:
            left.append(names[i])
    print('SET', index)
    for name in left:
        print(name)
    for name in right[::-1]:
        print(name)
    n = int(sys.stdin.readline())
    index += 1
