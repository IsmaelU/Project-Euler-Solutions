# Project Euler Problem 20 - Factorial Digit Sum
# https://projecteuler.net/problem=20
# Answer = 648

def question():
    print( """
    Project Euler Problem 20:

    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
    """)

def factorial(num):
    """
    Calculate the factorial of a given number.

    Args:
        num (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the input number.

    Time Complexity:
        O(num) - This is a recursive function that calls itself 'num' times.
    """
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def sum_of_digits(num):
    """
    Calculate the sum of the digits of a given number.

    Args:
        num (int): The number to calculate the sum of digits for.

    Returns:
        int: The sum of the digits of the input number.

    Time Complexity:
        O(log10(num)) - The number of digits in 'num' determines the number of iterations.
    """
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum

def solve(num):
    """
    Solve Project Euler Problem 20: Find the sum of the digits in the factorial of a number.

    Args:
        num (int): The number for which to calculate the factorial and sum the digits.

    Returns:
        int: The sum of the digits of the factorial of the input number.
    """
    factorial_result = factorial(num)
    return sum_of_digits(factorial_result)

def main():
    question()
    num = 100 
    result = solve(num)
    print(f"The sum of the digits in the factorial of {num} is: {result}")

if __name__ == "__main__":
    main()
