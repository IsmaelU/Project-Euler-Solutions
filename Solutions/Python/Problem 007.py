# Project Euler Problem 7 - 10001st prime
# https://projecteuler.net/problem=7
# Answer = 104743

def question():
    print("What is the 10001st prime number?")

def is_prime(num):
    """
    Check if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    for i in range(2, (int(num ** 0.5)+1)):
        if (num % i) == 0:
            return False
    return True

def is_prime_optimised(num):
    """
    Check if a number is prime. Only test divisibility by 2 and by just the odd numbers between 3 and Square Root of N, since divisibility by an even number implies divisibility by 2.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False

    return True

def prime_list():
    """
    Find the 10001st prime number.

    Time Complexity: O(n * sqrt(m)), where n is the number of iterations to find the 10001st prime, and m is the value of the number being checked for primality.

    Returns:
        int: The 10001st prime number.
    """
    prime_list = []
    num = 2
    while True:
        if is_prime_optimised(num):
            prime_list.append(num)
        if len(prime_list) == 10001:
            return prime_list[-1]
        num += 1

def main():
    """
    Main function to execute the problem-solving process.
    """
    question()
    result = prime_list()
    print(f"The 10001st prime number is {result}.")

if __name__ == "__main__":
    main()
