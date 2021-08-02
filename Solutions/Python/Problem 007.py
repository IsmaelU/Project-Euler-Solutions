# Project Euler Problem 7- 10001st prime
# https://projecteuler.net/problem=7
# Answer = 104743


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def prime_list():
    prime_list = []
    num = 2
    while True:
        if is_prime(num):
            prime_list.append(num)
        if len(prime_list) == 10001:
            return(prime_list[-1])
            break
        num += 1


print(prime_list())
