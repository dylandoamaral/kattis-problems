import sys

n = int(sys.stdin.readline())

index, t_n, t_o, t_e = 1, 0, 0, 0
for iteration in range(0, n):
    line = sys.stdin.readline().strip().split()
    m = int(line[1])
    if index < m:
        t = t_n
        t_odd = t_o
        t_even = t_e
        for i in range(index + 1, m + 1):
            t += i
            t_odd += i * 2 - 1
            t_even += i * 2
    else:
        t = 0
        t_odd = 0
        t_even = 0
        for i in range(1, m + 1):
            t += i
            t_odd += i * 2 - 1
            t_even += i * 2
    if t > t_n:
        index, t_n, t_o, t_e = m, t, t_odd, t_even

    print(line[0], t, t_odd, t_even)
