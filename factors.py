#!/usr/bin/python3

import sys

def factorize_number(number):
    factors = []
    for i in range(2, number//2 + 1):
        if number % i == 0:
            factors.append((i, number//i))
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                factorizations = factorize_number(number)
                for factorization in factorizations:
                    print(f"{number}={factorization[0]}*{factorization[1]}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == '__main__':
    main()
