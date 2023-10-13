// Problem 5 - Largest palindrome product
// https://projecteuler.net/problem=5
// Answer = 232792560  

fn question() {
    println!("What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?");
}

fn is_divisible_by_range(num: i32) -> bool {
    // Check if a number is divisible by all numbers from 11 to 19
    for i in 11..20 {
        if num % i != 0{
            return false;
        }
    }
    true
}

fn find_smallest_multiple(num: i32) -> i32 {
    // Find the smallest positive number that is evenly divisible by all numbers from 1 to 'num'.
    let mut answer = num;
    loop {
        if is_divisible_by_range(answer){
            break;
        } else {
            answer += num
        }
    }
    answer
}

fn main() {
    question();
    let result = find_smallest_multiple(20);
    println!("The smallest positive number divisible by all numbers from 1 to 20 is: {}", result);
}
