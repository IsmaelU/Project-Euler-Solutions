# Project Euler Problem 16 - Power Digit Sum
# https://projecteuler.net/problem=16
# Answer = 1366

def question():
    """
    Print the problem statement.
    """
    print("""Find the sum of the digits of the result of 2^1000.""")

def solve(base, exponent):
    """
    Calculate the result of base^exponent and return the sum of its digits.
    Time Complexity: O(log(exponent))

    Args:
        base (int): The base number.
        exponent (int): The exponent.

    Returns:
        int: The sum of the digits of base^exponent.
    """
    num_list = map(int, str(pow(base, exponent)))
    return sum(num_list)

def main():
    question()
    result = solve(2, 1000)
    print(f"The answer is {result}")

if __name__ == "__main__":
    main()
