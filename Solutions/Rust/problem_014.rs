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

fn get_chain_length(start: u64, cache: &mut [Option<u32>]) -> u32 {
    if start == 1 {return 1;}

    if start < cache.len() as u64{
        match cache[start as usize]{
            Some(val) => {
                return val
            },
            None => {
                let next_num = next_collatz(start);
                let counter = get_chain_length(next_num, cache) + 1;

                cache[start as usize] = Some(counter);
                return counter
            }
        }
    }else{
        let next_num = next_collatz(start);
        let counter = get_chain_length(next_num, cache) + 1;

        return counter
    }
}

fn solve(limit: usize) -> u32 {
    let mut max_length = 0;
    let mut best_start = 0;
    let mut cache = vec![None; limit];

    for i in (limit / 2)..limit{
        let current_length = get_chain_length(i as u64, &mut cache);
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