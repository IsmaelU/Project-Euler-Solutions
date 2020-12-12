#!/usr/bin/python3.8

# Problem 1- Multiples of 3 and 5
# https://projecteuler.net/problem=1
# Answer = 233168

def multiple():
    answer=0
    for i in range(1,1000):
        if i%3==0 or i%5==0:
            answer = answer + i
    return(answer)

print(multiple())
