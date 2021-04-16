#!/usr/bin/python3

# Project Euler Problem 9 - Special Pythagorean triplet
# https://projecteuler.net/problem=9
# Answer =

def main():
    a = 1
    b = 1
    while True:
        c = (a**2) + (b**2)
        if c % 1 == 0:
            print(f"{a}2 + {b}2 = {c}2")
        b += 1

def sqrt(num):
    return
