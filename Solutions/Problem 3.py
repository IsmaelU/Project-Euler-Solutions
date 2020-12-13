#!/usr/bin/python3.8

# Problem 3- Largest prime factor
# https://projecteuler.net/problem=3
# Answer = 

def largestprimefactor(num):
    factors = (i for i in range(1,num) if num % i == 0)
    return(factors)                  

print(largestprimefactor(5555))
