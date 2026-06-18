// Problem 4 - Largest palindrome product
// https://projecteuler.net/problem=4
// Answer = 906609

fn question() {
    println!("Find the largest palindrome made from the product of two 3-digit numbers.");
}

fn is_palindrome(num:i32) -> bool{
    let mut reverse_num = 0;
    let mut temp_num = num;
    while temp_num != 0{
        reverse_num = (reverse_num * 10) + (temp_num % 10);
        temp_num /= 10;
    }
    reverse_num == num
}

fn find_largest_palindrome() -> i32 {
    // Finds the largest palindrome made from the product of two 3-digit numbers.
    // Time complexity: O(n^2), where 'n' is the range (100 to 999) for the numbers being multiplied.
    let mut largest_palindrome = 0;

    for i in (100..1000).rev() {
        if i * 1000 < largest_palindrome{
            break
        }
        for j in (i..1000).rev() {
            let product = i * j;
            if product < largest_palindrome{
                break;
            }
            if is_palindrome(product) {
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

