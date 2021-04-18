# Project Euler Problem 9 - Special Pythagorean triplet
# https://projecteuler.net/problem=9
# Answer = 31875000

def question():
    print("A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, \na^2 + b^2 = c^2 \nFor example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2. \nThere exists exactly one Pythagorean triplet for which a + b + c = 1000. \nFind the product abc.")

def solve(num):
    a = 1
    b = 1
    while True:
        if a > b:
            b += 1
            a = 1
        c = ((a ** 2) + (b**2)) ** 0.5
        if sum((a,b,c)) == num:
            return int(a * b * c)
        a += 1

def main():
    question()
    print(f"The answer is {solve(1000)}")

main()
