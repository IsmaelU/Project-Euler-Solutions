#!/usr/bin/python3.8

# Problem 2- Even Fibonacci numbers
# https://projecteuler.net/problem=2
# Answer = 

# First Solution
def fibonacci():
    a = 1
    b = 1
    fib_list = []
    c = 0
    while c < 4000000:
        fib_list.append(b)
        c = a+b
        a = b
        b = c
    return(sum([i for i in fib_list if i%2 == 0]))
print(fibonacci())


# Second Solution
def fibonacci2():
    fib_numbers = [1,2]
    while fib_numbers[-1] < 4000000:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    del fib_numbers[-1]
    return(sum([i for i in fib_numbers if i%2 == 0]))
print(fibonacci2())
