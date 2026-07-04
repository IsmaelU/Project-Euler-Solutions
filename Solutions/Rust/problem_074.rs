// Problem 74 - Digit factorial chains
// https://projecteuler.net/problem=74
// Answer = 402

const FACTORIALS: [u64; 10] = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880];

fn question() {
    println!("How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?");
}

fn next_factorial_sum(mut num: u64) -> u64 {
    if num == 0 {
        return 1;
    }
    let mut next_factorial_sum = 0;
    while num != 0 {
        let digit = (num % 10) as usize;
        next_factorial_sum += FACTORIALS[digit];
        num /= 10;
    }
    next_factorial_sum
}

fn get_chain_length(start: u64, history: &mut Vec<u64>, cache: &mut [u32]) -> u32 {
    if history.contains(&start) {
        if let Some(index) = history.iter().position(|&x| x == start) {
            let loop_length = history.len() as u32 - index as u32;
            for &i in &history[index..] {
                if i < cache.len() as u64 {
                    cache[i as usize] = loop_length;
                }
            }
            return loop_length;
        }
    }

    if start >= cache.len() as u64 {
        history.push(start);
        let next_num = next_factorial_sum(start);
        let result = get_chain_length(next_num, history, cache);
        return result + 1;
    }
    match cache[start as usize] {
        0 => {
            history.push(start);
            let next_num = next_factorial_sum(start);
            let result = get_chain_length(next_num, history, cache);
            if cache[start as usize] != 0 {
                return cache[start as usize];
            }
            cache[start as usize] = result + 1;
            return result + 1;
        }
        _ => return cache[start as usize],
    }
}

fn solve(limit: usize) -> u32 {
    let mut target_chains_count = 0;
    let mut cache = vec![0; limit];
    let mut history = vec![];

    for i in 1..limit {
        history.clear();
        if get_chain_length(i as u64, &mut history, &mut cache) == 60 {
            target_chains_count += 1;
        }
    }

    target_chains_count
}

fn main() {
    question();
    println!("Answer = {}", solve(1_000_000));
}
