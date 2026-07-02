// Problem 5 - Smallest Multiple
// https://projecteuler.net/problem=5
// Answer = 232792560  

fn question() {
    println!("What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?");
}

fn gcf(mut a: u64, mut b: u64) -> u64 {
    // Returns Greatest Common Factor of a and b
    while b != 0 {
        (a,b) = (b, a % b);
    }
    a
}

fn lcm(a: u64, b: u64) -> u64 {
    // Returns Lowest Common Multiple of a and b
    (a*b)/gcf(a,b)
}

fn solve(num:u64) -> u64{
    (1..=num).fold(1, lcm)
}

fn main() {
    question();
    println!("The smallest positive number divisible by all numbers from 1 to 20 is: {}", solve(20));
}
