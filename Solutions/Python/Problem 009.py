# Project Euler Problem 9 - Special Pythagorean triplet
# https://projecteuler.net/problem=9
# Answer = 31875000

def question():
    print("""
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """)

def generate(m, n):
    """
    Generate a Pythagorean triplet using Euclid's Formula.

    Args:
        m (int): A positive integer.
        n (int): A positive integer, smaller than 'm'.

    Returns:
        tuple: A Pythagorean triplet (a, b, c) where a < b < c.
    """
    a = 2 * m * n
    b = m**2 - n**2
    c = m**2 + n**2
    return a, b, c

def solve(num):
    """
    Find the product of the Pythagorean triplet (a, b, c) for which a + b + c = 'num'.

    Args:
        num (int): The desired sum of the triplet.

    Returns:
        int: The product of the Pythagorean triplet.
    """
    m = 2
    n = 1
    while sum(generate(m, n)) != num:
        if m == n:
            m += 1
            n = 1
        n += 1
    triplet = generate(m, n)
    return triplet[0] * triplet[1] * triplet[2]

def main():
    question()
    print(f"The answer is {solve(1000)}")

if __name__ == "__main__":
    main()
