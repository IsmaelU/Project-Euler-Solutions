// Problem 5 - Largest palindrome product
// https://projecteuler.net/problem=5
// Answer = 

fn question() {
    println!("What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?");
}

fn check_multiple(num: i32) -> bool {
    // Check if a number is divisible by all numbers from 11 to 19
    for i in 11..19 {
        if num % i != 0{
            return false;
        }
    }
    true
}

fn solve(num: i32) -> i32 {
    // Find the smallest positive number that is evenly divisible by all numbers from 1 to 'num'.
    let mut answer = num;
    while true {
        if check_multiple(answer){
            break;
        } else {
            answer += num
        }
    }
    answer
}

fn main() {
    question();
    let result = solve(20);
    println!("The smallest positive number divisible by all numbers from 1 to 20 is: {}", result);
}