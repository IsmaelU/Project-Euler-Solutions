# Project Euler Problem 6 - Sum Square Difference
# https://projecteuler.net/problem=6
# Answer = 25164150

def question():
    print("""
    Find the difference between the sum of the squares of the first one hundred natural numbers and
    the square of the sum.
    """)

def sum_of_squares_difference(n):
    """
    Calculate the difference between the square of the sum and the sum of squares of the first 'n' natural numbers.

    Time Complexity: O(n)

    Args:
        n (int): The upper limit of natural numbers.

    Returns:
        int: The difference between the square of the sum and the sum of squares.
    """
    sum_of_squares = sum(i ** 2 for i in range(1, n + 1))
    square_of_sum = sum(range(1, n + 1)) ** 2
    return square_of_sum - sum_of_squares

def main():
    question()
    print("Answer =", sum_of_squares_difference(100))

if __name__ == "__main__":
    main()