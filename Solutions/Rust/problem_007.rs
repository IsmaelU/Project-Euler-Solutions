// Problem 7 - 10001st prime
// https://projecteuler.net/problem=7
// Answer = 104743

fn question() {
    println!("What is the 10001st prime number?")
}

fn is_prime(n: u32) -> bool {
    if n <= 1 { return false; }
    if n <= 3 { return true; }
    if n % 2 == 0 || n % 3 == 0 { return false; }

    let mut i = 5;
    while i <= n / i {

        if n % i == 0 || n % (i + 2) == 0 {
            return false;
        }
        i += 6;
    }

    true
}

fn solve(bound:u32) -> u32{
    if bound == 1 { return 2; }
    if bound == 2 { return 3; }
    let mut counter = 2;
    let mut i = 3;
    while counter < bound{
        i += 2;
        if is_prime(i){
            counter += 1;
        }
    }
    i
}

fn main() {
    question();
    println!("Answer = {}", solve(10001));
}
