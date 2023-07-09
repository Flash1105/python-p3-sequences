#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = []

    if length >= 1:
        fibonacci.append(0)
    if length >= 2:
        fibonacci.append(1)

    while len(fibonacci) < length:
        next_num = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_num)

    print(fibonacci)
