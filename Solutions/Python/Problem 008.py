# Project Euler Problem 8 - Largest product in a series
# https://projecteuler.net/problem=8
# Answer = 23514626000

def question():
    print("""
    Find the largest product of 13 adjacent digits in the given series.
    """)

def split_list(num_list):
    """
    Split a string of digits into a list of integers.

    Args:
        num_list (str): A string of digits.

    Returns:
        list: A list of integers.
    """
    return [int(num) for num in num_list]

def multiple_list(num_list):
    """
    Calculate the product of all numbers in a list.

    Args:
        num_list (list): A list of integers.

    Returns:
        int: The product of the numbers in the list.
    """
    answer = 1
    for i in num_list:
        answer *= i
    return answer

def main():
    """
    Main function to find the largest product of 13 adjacent digits in a series.

    Returns:
        int: The largest product.
    """
    series = str(731671765313306249192251196744265747423553491993496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
    top_list = 1
    for i in range(1000):
        adjacent_digits = split_list(series[i:i+13])
        if 1 in adjacent_digits or 0 in adjacent_digits:
            continue
        if multiple_list(adjacent_digits) > top_list:
            top_list = multiple_list(adjacent_digits)
    return top_list

if __name__ == "__main__":
    question()
    print(f"The answer is {main()}.")
