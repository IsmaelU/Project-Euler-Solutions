# Problem 1- Multiples of 3 and 5
# https://projecteuler.net/problem=1
# Answer = 233168

def question():
    print("Find the sum of all the multiples of 3 or 5 below 1000.")


def solve(bound):
    return sum(i for i in range(1,bound) if i % 3 == 0 or i % 5 == 0)

#def SumDivisbleBy(n , p):
#    return int(n*(p/n)*((p/n)+1)/2)

#def solve1(bound):
#    return SumDivisbleBy(3,bound-1) + SumDivisbleBy(5,bound-1) - SumDivisbleBy(15,bound-1)

def main():
    question()
    print(solve(1000))
    #print(solve1(1000))

main()
