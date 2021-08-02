# Problem 1- Summation of primes
# https://projecteuler.net/problem=10
# Answer =


def question():
    print("""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.""")


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_lister(bound):
    prime_list = []
    for num in range(bound):
        if is_prime(num):
            prime_list.append(num)
    return prime_list


def solve(bound):
    prime_list = prime_lister(bound)
    return sum(prime_list)


def main():
    question()
    print(f"The answer is {solve(2000000)}")


main()
