# Problem 4- Largest palindrom product
# https://projecteuler.net/problem=4
# Answer = 906609

def palindrome():
    palindromes = []
    for i in range(1000):
        for f in range(1000):
            answer = i * f
            if str(answer) == str(answer)[::-1]:
                palindromes.append(answer)
    return(max(palindromes))


print(palindrome())
