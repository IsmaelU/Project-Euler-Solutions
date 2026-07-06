// Problem 36 - Double-base palindromes
// https://projecteuler.net/problem=36
// Answer = 872187

fn question() {
    println!("Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.");
}

fn is_base10_palindrome(num: u32) -> bool {
    let mut reverse_num = 0;
    let mut temp_num = num;
    while temp_num != 0{
        reverse_num = (reverse_num * 10) + (temp_num % 10);
        temp_num /= 10;
    }
    reverse_num == num
}

fn is_base2_palindrome(num: u32) -> bool{
    if num == 0{
        return true
    }
    let reverse_num = num.reverse_bits() >> num.leading_zeros();
    reverse_num == num
}

fn solve(limit: u32) -> u32 {
    //Step by 2 as even numbers can never be a palindrome in base 2
    (1..limit).step_by(2).filter(|&x| is_base2_palindrome(x) && is_base10_palindrome(x)).sum()
}

fn main() {
    question();
    let limit = 1_000_000;
    println!("Answer = {}", solve(limit));
}