# Problem 12 - Highly divisible triangular number
# https://projecteuler.net/problem=12
# Answer = 76576500

# Import math module for sqrt function
import math

def question():
    print("""
    Explanation of the problem:
    
    The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number 
    would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

        1: 1
        3: 1, 3
        6: 1, 2, 3, 6
        10: 1, 2, 5, 10
        15: 1, 3, 5, 15
        21: 1, 3, 7, 21
        28: 1, 2, 4, 7, 14, 28

    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred divisors?
    """)

def generate_triangle_number(num):
    """
    Generates the nth triangle number.
    
    Args:
        num (int): The term of the triangle number to generate.
        
    Returns:
        int: The nth triangle number.
    """
    return sum(i for i in range(1, num + 1))

def count_divisors(num):
    """
    Counts the number of divisors for a given number.
    
    Args:
        num (int): The number to count divisors for.
        
    Returns:
        int: The count of divisors for the given number.
    """
    count = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            count += 2 if i != num // i else 1  # Count both i and num/i as divisors if they are different.
    return count

def find_triangle_with_divisors(target_divisors):
    """
    Finds the first triangle number with over a certain number of divisors.
    
    Args:
        target_divisors (int): The minimum number of divisors to search for.
        
    Returns:
        int: The first triangle number with over `target_divisors` divisors.
    """
    term = 1
    while True:
        triangle_num = generate_triangle_number(term)
        if count_divisors(triangle_num) > target_divisors:
            return triangle_num
        term += 1

def main():
    question()
    target_divisors = 500
    answer = find_triangle_with_divisors(target_divisors)
    print(f"The answer is {answer}")

if __name__ == "__main__":
    main()
