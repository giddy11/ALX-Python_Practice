#!/usr/bin/python3

def print_last_digit(number):
    number = abs(number) % 10
    print(f"{number}", end="")
    return number


print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)