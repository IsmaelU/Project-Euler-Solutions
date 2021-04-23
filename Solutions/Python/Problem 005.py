#Problem 5- Smallest multiple
# https://projecteuler.net/problem=5
# Answer = 21162960 

def question():
    print("""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """)


# Solution 1
def multiple(number):
    for i in range(19,11,-1):
        if number  % i != 0:
                return False
    return True

def solve(num):
    answer = num
    while True:
        if multiple(answer):
            break
        else:
            answer += num
    return answer

# Solution 2

def main():
    question()
    print(f"The answer is {solve(20)}")

main()
