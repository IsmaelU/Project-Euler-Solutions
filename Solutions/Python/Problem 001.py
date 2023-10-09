# Problem 1 - Multiples of 3 and 5
# https://projecteuler.net/problem=1
# Answer = 233168

def question():
    print("Find the sum of all the multiples of 3 or 5 below 1000.")

def solve(bound):
    """
    Calculate the sum of all multiples of 3 or 5 below a given bound using a list comprehension.
    
    Time Complexity: O(n)
    
    Args:
        bound (int): The upper bound for finding multiples.

    Returns:
        int: The sum of all multiples of 3 or 5 below the given bound.
    """
    return sum(i for i in range(1, bound) if i % 3 == 0 or i % 5 == 0)

def SumDivisibleBy(n, p):
    """
    Calculate the sum of all multiples of 'n' below 'p' using the arithmetic progression formula.
    
    Time Complexity: O(1)
    
    Args:
        n (int): The divisor.
        p (int): The upper bound for finding multiples.

    Returns:
        int: The sum of all multiples of 'n' below 'p'.
    """
    return int(n * (p // n) * ((p // n) + 1) // 2)

def solve1(bound):
    """
    Calculate the sum of all multiples of 3 or 5 below a given bound using the SumDivisibleBy function.
    
    Time Complexity: O(1)
    
    Args:
        bound (int): The upper bound for finding multiples.

    Returns:
        int: The sum of all multiples of 3 or 5 below the given bound.
    """
    return SumDivisibleBy(3, bound - 1) + SumDivisibleBy(5, bound - 1) - SumDivisibleBy(15, bound - 1)

def main():
    question()
    print("Solution 1 (List Comprehension):", solve(1000))
    print("Solution 2 (Arithmetic Progression Formula):", solve1(1000))
    print("The second solution is generally more efficient for larger bounds due to its mathematical nature.")

if __name__ == "__main__":
    main()
