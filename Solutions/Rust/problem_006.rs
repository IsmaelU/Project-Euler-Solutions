// Problem 6 - Largest palindrome product
// https://projecteuler.net/problem=6
// Answer = 

fn question() {
    println!("Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.");
}


def solve(num:i32) -> i32{
    let sum_of_squares = [i **2; for i in 1..n].iter().sum();
    let square_of_sum = [for i in 1..n].iter().sum() ** 2
    square_of_sum - sum_of_squares
}

fn main() {
    question();
    let result = solve(100);
    println!("Answer = ", result);
}