// Problem 92 - Square digit chains
// https://projecteuler.net/problem=92
// Answer = 8581146

fn question() {
    println!("How many starting numbers below ten million will arrive at 89?");
}

fn get_next_chain_link(mut num: u32) -> u32 {
    let mut next_chain_num = 0;
    while num != 0{
        next_chain_num += (num % 10).pow(2);
        num /= 10;
    }
    next_chain_num
}

fn arrives_at_89(mut num: u32, cache: &mut [Option<bool>]) -> bool { 
    // 1. Shrink num if it is outside the cache bounds
    while num >= cache.len() as u32 {
       num = get_next_chain_link(num); 
    }

    // 2. Base cases
    if num == 89 { return true; }
    if num == 1 { return false; }

    // 3. Cache lookup
    match cache[num as usize] {
        Some(val) => val,
        None => {
            // 4. Cache miss: find the next link and recurse
            // Using recursion as practise for eventual chess bot even though loop way seems to run faster with cache
            let next_num = get_next_chain_link(num);
            let result = arrives_at_89(next_num, cache);
            
            cache[num as usize] = Some(result);
            return result
        }
    }
}

fn solve(limit: u32) -> usize {
    let max_size:usize = (get_next_chain_link(limit - 1) + 1) as usize;
    let mut cache = vec![None; max_size];
    (1..limit).filter(|&x| arrives_at_89(x, &mut cache)).count()
}

fn main() {
    question();
    let limit = 10_000_000;
    println!("Answer = {}", solve(limit));
}