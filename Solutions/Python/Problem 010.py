import math

def question():
    print("""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.""")

def sieve_of_eratosthenes(num):
    """
    Sieve of Eratosthenes: Find all prime numbers up to the given limit.
    Time Complexity: O(n * log(log(n))), where 'n' is the upper limit or the range of numbers up to which you want to find prime numbers.

    Args:
        num (int): The upper limit for finding prime numbers.

    Returns:
        int: The sum of all prime numbers below the limit.
    """
    base = 2
    num_list = list(range(2, num))
    while base * base < num:
        num_list = [i for i in num_list if i % base != 0 or i == base]
        base += 1
    return sum(num_list)

def sieve_of_sundaram(num):
    """
    Sieve of Sundaram: Find all prime numbers up to the given limit.
    Time Complexity: O(n * log(log(n))), where 'n' is the upper limit or the range of numbers up to which you want to find prime numbers.

    Args:
        num (int): The upper limit for finding prime numbers.

    Returns:
        int: The sum of all prime numbers below the limit.
    """
    bound = (num - 2) // 2
    print(bound)

def sieve_of_atkins(num):
    """
    Sieve of Atkins: Find all prime numbers up to the given limit.
    Time Complexity: O(n / log(log(n))), where 'n' is the upper limit

    Args:
        num (int): The upper limit for finding prime numbers.

    Returns:
        int: The sum of all prime numbers below the limit.
    """
    return True

def main():
    question()
    bound = 2000000
    print(f"The answer is {sieve_of_eratosthenes(bound)}")
    # Print("Explanation about the 3 sieves")

if __name__ == "__main__":
    main()
