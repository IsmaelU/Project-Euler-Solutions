# Project Euler Problem 3 - Largest Prime Factor
# https://projecteuler.net/problem=3
# Answer: 6857

import math
import itertools

def question():
    print("What is the largest prime factor of the number 600851475143?"

def is_prime(num):
    """
    Check if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    for i in range(2, (int(math.sqrt(num))+ 1)):
        if (num % i) == 0:
            return False
    return True

def factor_pairs(number):
    """
    Generate pairs of factors for the given number.

    Args:
        number (int): The number for which to generate factor pairs.

    Yields:
        tuple: A pair of factors (factor1, factor2).
    """
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            yield (i, number // i)

def largest_prime_factor(number):
    """
    Finds the largest prime factor of the given number.

    Args:
        number (int): The number for which to find the largest prime factor.

    Returns:
        int: The largest prime factor of the given number.
    """
    factors = list(itertools.chain.from_iterable(factor_pairs(number)))
    factors.sort(reverse=True)
    for factor in factors:
        if is_prime(factor):
            return factor

def main():
    question()
    number_to_factor = 600851475143
    largest_factor = largest_prime_factor(number_to_factor)
    print(f"The answer is {largest_factor}")

if __name__ == "__main__":
    main()

