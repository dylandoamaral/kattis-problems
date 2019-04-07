import sys


def total_digits(number):
    n_string = str(number)
    total = 0
    for digit in n_string:
        total += int(digit)
    return total


n = int(sys.stdin.readline())

while n != 0:
    p = 11
    np = n * p
    while total_digits(n) != total_digits(np):
        p += 1
        np = n * p
    print(p)
    n = int(sys.stdin.readline())
