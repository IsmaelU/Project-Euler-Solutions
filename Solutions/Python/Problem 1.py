# Problem 1- Multiples of 3 and 5
# https://projecteuler.net/problem=1
# Answer = 233168

def question():
    print("Find the sum of all the multiples of 3 or 5 below 1000.")


def compute(bound):
    return sum(i for i in range(1,bound) if i % 3 == 0 or i % 5 == 0)

def main():
    question()
    print(compute(1000))

main()
