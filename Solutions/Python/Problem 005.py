# Problem 5 - Smallest multiple
# https://projecteuler.net/problem=5
# Answer = 21162960

def question():
    print("""
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """)

# Solution 1
def is_multiple(number):
    """
    Check if a number is divisible by all numbers from 11 to 19.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is divisible by all numbers from 11 to 19, False otherwise.
    """
    for i in range(19, 10, -1):
        if number % i != 0:
            return False
    return True

def find_smallest_multiple(num):
    """
    Find the smallest positive number that is evenly divisible by all numbers from 1 to 'num'.

    Args:
        num (int): The upper limit for divisibility.

    Returns:
        int: The smallest positive number that meets the criteria.
    """
    answer = num
    while True:
        if is_multiple(answer):
            break
        else:
            answer += num
    return answer

def main():
    question()
    smallest_multiple = find_smallest_multiple(20)
    print(f"The smallest positive number divisible by all numbers from 1 to 20 is {smallest_multiple}.")

if __name__ == "__main__":
    main()
