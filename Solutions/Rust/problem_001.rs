// Problem 1- Multiples of 3 and 5
// https://projecteuler.net/problem=1
// Answer = 233168

fn question() {
    println!("Find the sum of all the multiples of 3 or 5 below 1000.")
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

fn sum_multiples_up_to(number: u64, bound: u64) -> u64 {
    // Returns sum of all the multiples up to a bound using Arithmetic Progression Formula
    number * (bound / number) * ((bound / number) + 1) / 2
}

fn solve(a:u64, b:u64, bound:u64) -> u64 {
    // Returns sum of multiples of two numbers up to a given bound
    let limit = bound - 1;
    sum_multiples_up_to(a,limit) + sum_multiples_up_to(b,limit) - sum_multiples_up_to(lcm(a,b),limit)
}

fn main() {
    question();
    println!("{}", solve(3,5,1000));
}



// Old iterative solve function: 
//fn solve(bound: i32) -> i32 {
//   let mut answer = 0;
//    for n in 1..bound {
//        if n % 3 == 0 || n % 5 == 0 {
//            answer = answer + n;
//        }
//    }
//    answer
//}