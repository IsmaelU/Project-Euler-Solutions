// Problem 3 - Largest Prime Factor
// https://projecteuler.net/problem=3
// Answer = 6857

fn question() {
    println!("What is the largest prime factor of the number 600851475143?")
}

fn solve(mut num:u64) -> u64{
    let mut divisor = 1;
    while divisor <= num / divisor{
        divisor += 1;
        while num % divisor == 0{
            num /= divisor;
        }      
    }
    if num > 1 {num} else {divisor}
}

fn main() {
    question();
    println!("Answer = {}", solve(600851475143));
}