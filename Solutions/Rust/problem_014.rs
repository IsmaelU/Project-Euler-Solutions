// Problem 14 - Longest Collatz sequence
// https://projecteuler.net/problem=14
// Answer = 837799

fn question() {
    println!("Which starting number, under one million, produces the longest Collatz sequence?");
}

fn next_collatz(n: u64) -> u64 {
    // Uses bitwise operators to be more efficient than modulos and Integer division
    if (n & 1) == 1{
        (3 * n) + 1
    }else{
        n >> 1
    }
}

fn get_chain_length(mut start: u64) -> u32 {
    let mut counter = 1;
    loop{
        if start == 1{
            return counter
        }
        start = next_collatz(start);
        counter += 1;
    }
}

fn solve(limit: usize) -> u32 {
    let mut max_length = 0;
    let mut best_start = 0;

    for i in (limit / 2)..limit{
        let current_length = get_chain_length(i as u64);
        if current_length > max_length{
            best_start = i;
            max_length = current_length;
        }
    }
    best_start as u32
}

fn main() {
    question();
    println!("Answer = {}", solve(1_000_000));
}