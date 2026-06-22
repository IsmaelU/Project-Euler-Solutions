// Problem 10 - Summation of primes
// https://projecteuler.net/problem=10
// Answer = ?

fn question() {
    println!("Find the sum of all the primes below two million.");
}

fn solve(limit: usize) -> u64 {
    // Phase 1: Allocation & Initialisation
    // Allocate a contiguous bitmask/boolean block representing numbers up to `limit`
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
    is_prime.into_iter().enumerate().filter().map(num as u64).sum()
    // Phase 2: Sieve Execution Path
    // Implement the stride loop to cross off composite indices up to sqrt(limit)

    // Phase 3: Zero-Allocation Aggregation
    // Use iterator chains to filter indices and calculate the final u64 sum

    todo!()
}

fn main() {
    question();
    let limit = 2_000_000;
    println!("Answer = {}", solve(limit));
}
