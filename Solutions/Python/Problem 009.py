# Project Euler Problem 9 - Special Pythagorean triplet
# https://projecteuler.net/problem=9
# Answer = 31875000
from math import prod


def question():
    print("""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
""")


""" This solution uses Euclid's Formula for finding Pythagorean Triplets:
    Given any positive integers m and n where m > n > 0
    a = 2mn
    b = m^2 - n^2
    b = m^2 + n^2
"""


def generate(m, n):
    a = 2 * m * n
    b = (m ** 2) - (n ** 2)
    c = (m ** 2) + (n ** 2)
    return(a, b, c)


def solve(num):
    m = 2
    n = 1
    while sum(generate(m, n)) != num:
        if m == n:
            m += 1
            n = 1
        n += 1
    return prod(generate(m, n))


def main():
    question()
    print(f"The answer is {solve(1000)}")


main()
