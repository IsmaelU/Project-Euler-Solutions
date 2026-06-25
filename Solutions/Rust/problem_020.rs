// Problem 20 - Factorial Digit Sum
// https://projecteuler.net/problem=20
// Answer = 

use num_bigint::{BigUInt, Sign};

fn question() {
    println!("Find the sum of the digits in the number 100!.");
}



fn solve(factorial_num: usize) -> BigUInt {
    let mut factorial_result: BigUInt = 1;
    for i in 1..=factorial_num{
        factorial_result *= i as u32;
        println!("{}", factorial_result);
    }
    factorial_result
}

fn main() {
    question();
    println!("Answer = {}", solve(100));
}
