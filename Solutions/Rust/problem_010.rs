// Problem 10 - Summation of primes
// https://projecteuler.net/problem=10
// Answer = 142913828922

fn question() {
    println!("Find the sum of all the primes below two million.");
}

fn solve(limit: usize) -> u64 {
    let mut is_prime = vec![true; limit];
    is_prime[0] = false;
    is_prime[1] = false;

    let mut i: usize = 2;
    while i * i < limit {
        if is_prime[i] {
            for j in (i * i..limit).step_by(i) {
                is_prime[j] = false;
            }
        }
        i += 1;
    }

    is_prime.into_iter().enumerate().filter_map(|(index, is_prime)| is_prime.then_some(index as u64)).sum()
}

fn main() {
    question();
    let limit = 2_000_000;
    println!("Answer = {}", solve(limit));
}
