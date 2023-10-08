# Project Euler Problem 14 - Longest Collatz sequence
# https://projecteuler.net/problem=14
# Answer = 837799 which has a length of 525

def question():
    """
    Explanation of the problem:

    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?
    """

def collatz_sequence_length(num):
    """
    Returns the length of a Collatz Sequence starting from the given number.

    Args:
        num (int): The starting number of the Collatz Sequence.

    Returns:
        int: The length of the Collatz Sequence.
    """
    sequence_length = 1
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        sequence_length += 1
    return sequence_length

def find_longest_collatz(bound):
    """
    Finds the starting number under the given bound that produces the longest Collatz sequence.

    Args:
        bound (int): The upper bound for the starting numbers to consider.

    Returns:
        tuple: A tuple containing the starting number and the length of its Collatz sequence.
    """
    longest_starting_number = 0
    longest_sequence_length = 0
    for i in range(1, bound):
        length = collatz_sequence_length(i)
        if length > longest_sequence_length:
            longest_starting_number = i
            longest_sequence_length = length
    return (longest_starting_number, longest_sequence_length)

def main():
    question()
    bound = 1000000
    result = find_longest_collatz(bound)
    print(f"The answer is {result[0]} which has a length of {result[1]}")

if __name__ == "__main__":
    main()

