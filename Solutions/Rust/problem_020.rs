// Problem 20 - Factorial Digit Sum
// https://projecteuler.net/problem=20
// Answer = 648

fn question() {
    println!("Find the sum of the digits in the number 100!.");
}

fn solve_factorial_digit_sum(target: usize) -> u32 {
    // Allocation Strategy: Pre-allocate to prevent heap thrashing.
    // 100! contains 158 digits
    let mut digits: Vec<u8> = Vec::with_capacity(160);
    digits.push(1); // Base case: 1! = 1

    // Main iterative multiplication pipeline
    for factor in 2..=target {
        let mut carry = 0;
        for digit in digits.iter_mut() {
            let product = (factor * (*digit as usize)) + carry;
            
            *digit = (product % 10) as u8;
            carry = product / 10;
        }

        while carry > 0 {
            digits.push((carry % 10) as u8);
            carry /= 10;
        }
    }

    digits.iter().map(|&d| d as u32).sum()
}

fn main() {
    let target = 100;
    question();
    println!("Sum of digits for {}! = {}", target, solve_factorial_digit_sum(target));
}