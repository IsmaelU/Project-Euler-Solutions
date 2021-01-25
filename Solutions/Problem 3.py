#!/usr/bin/python3
# Problem 3- Largest prime factor
# https://projecteuler.net/problem=3
# Answer = 6857

def prime_factors(factors):
    prime_list = []
    for factor in factors:
        prime = [i for i in range (2,factor) if factor % i == 0]
        if not prime: 
            prime_list.append(factor)
    return max(prime_list)


def largestprimefactor(num):
    factors = [i for i in range(1,num) if num % i == 0]
    return(prime_factors(factors))



print(largestprimefactor(600851475143))
