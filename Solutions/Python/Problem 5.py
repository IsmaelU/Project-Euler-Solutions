#Problem 5- Smallest multiple
# https://projecteuler.net/problem=5
# Answer = 21162960 

# Solution 1
def multiple(number):
    for i in range(19,11,-1):
        if number  % i != 0:
                return(False)
    return(True)

number = 20
while True:
    if multiple(number):
        break
    else:
        number += 20

print(number)

# Solution 2


