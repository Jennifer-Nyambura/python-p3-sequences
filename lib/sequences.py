#!/usr/bin/env python3


def print_fibonacci(n):
    if n <= 0:
        print([])  # print empty list for invalid input
        return

    # Start with the first two Fibonacci numbers
    fibonacci = [0, 1]

    # Generate Fibonacci numbers until we reach desired length
    while len(fibonacci) < n:
        next_value = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_value)

    # Slice in case n is 1
    print(fibonacci[:n])


#test the function
print_fibonacci(0)  # => []
print_fibonacci(1)  # => [0]
print_fibonacci(2)  # => [0, 1]
print_fibonacci(9)  # => [0, 1, 1, 2, 3, 5, 8, 13, 21]
