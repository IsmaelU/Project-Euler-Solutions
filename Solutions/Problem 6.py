#!/usr/bin/python3.8

# Project Euler Problem 6 - Sum Square Difference
# https://projecteuler.net/problem=6
# Answer = 25164150

def square1(num):
    answer = 0
    for i in range(1,num+1):
        answer += i
    return(answer**2)


def square2(num):
    answer = 0
    for i in range(1,num+1):
        answer += i ** 2
    return(answer)
print(square1(100)-square2(100))
