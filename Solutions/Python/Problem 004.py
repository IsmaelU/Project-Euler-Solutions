# Problem 4 - Largest palindrome product
# https://projecteuler.net/problem=4
# Answer = 906609

def palindrome():
    """
    Find the largest palindrome product of two 3-digit numbers using nested loops.

    Time Complexity: O(n^2), where n is the number of 3-digit numbers (900).

    Returns:
        int: The largest palindrome product.
    """
    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if str(product) == str(product)[::-1]:
                palindromes.append(product)
    return max(palindromes)

def main():
    largest_palindrome = palindrome()
    print(f"The largest palindrome product of two 3-digit numbers is {largest_palindrome}.")

if __name__ == "__main__":
    main()
