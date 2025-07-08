#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = []

    if length == 0:
        print(fibonacci)
    elif length == 1:
        fibonacci.append(0)
        print(fibonacci)
    else:
        fibonacci = [0, 1]
        while len(fibonacci) < length:
            next_number = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(next_number)
        print(fibonacci)

print_fibonacci(4)        
