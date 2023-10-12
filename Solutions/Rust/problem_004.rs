// Problem 4 - Largest palindrome product
// https://projecteuler.net/problem=4
// Answer = 906609

fn question() {
    println!("Find the largest palindrome made from the product of two 3-digit numbers.");
}

fn is_palindrome(n: i32) -> bool {
    // Checks if a number is a palindrome.
    // Time complexity: O(d), where 'd' is the number of digits in 'n'.
    let n_str = n.to_string();
    n_str == n_str.chars().rev().collect::<String>()
}

fn find_largest_palindrome() -> i32 {
    // Finds the largest palindrome made from the product of two 3-digit numbers.
    // Time complexity: O(n^2), where 'n' is the range (100 to 999) for the numbers being multiplied.
    let mut largest_palindrome = 0;

    for i in 100..1000 {
        for j in 100..1000 {
            let product = i * j;
            if is_palindrome(product) && product > largest_palindrome {
                largest_palindrome = product;
            }
        }
    }

    largest_palindrome
}

fn main() {
    question();
    let result = find_largest_palindrome();
    println!("The largest palindrome is: {}", result);
}

