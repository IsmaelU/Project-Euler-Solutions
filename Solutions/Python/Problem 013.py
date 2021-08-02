# Project Euler Problem 14 - Longest Collatz sequence
# https://projecteuler.net/problem-14
# Answer =

def question():
    print("""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
""")


def collatz(num):
    sequence = [num, ]
    while sequence[-1] != 1:
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1] / 2)
        else:
            sequence.append((3 * sequence[-1]) + 1)
    return len(sequence)


def solve(bound):
    longest_len = 0
    for i in range(0, bound):
        if collatz(i) > longest_len:
            longest = i
            longest_len = collatz(i)
    return(longest, longest_len)


def main():
    question()
    print(f"The answer is {solve(100)}")


main()
