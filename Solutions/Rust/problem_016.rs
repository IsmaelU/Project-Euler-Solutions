// Problem 16 - Power digit sum
// https://projecteuler.net/problem=16
// Answer = 1366

fn question() {
    println!("2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.");
    println!("What is the sum of the digits of the number 2^1000?");
}

/// Calculates the sum of the individual digits of 2 raised to a given power.
///
/// # Arguments
/// 
/// * `power` - The exponent to which the base 2 is raised.
///
/// # Returns
///
/// The scalar sum of all decimal digits in the resulting expansion.
fn solve(base:u32, power: u32) -> u32 {
    let capacity = (f64::from(power) * f64::from(base).log10()).ceil() as usize + 1;
    let mut power_answer: Vec<u8> = Vec::with_capacity(capacity);
    power_answer.push(1);
    for _exponent in 0..power{
        let mut carry = 0;
        for digit in power_answer.iter_mut(){
            let product = (base * (*digit as u32)) + carry;
            *digit = (product % 10) as u8;
            carry = product / 10;
        }
        while carry > 0 {
            power_answer.push((carry % 10) as u8);
            carry /= 10;
        }
    }
    power_answer.iter().map(|&x| x as u32).sum()
}

fn main() {
    question();
    let result = solve(2, 1000);
    println!("Answer = {}", result);
}


// TODO: Implement macro-stepping optimization by finding the maximum 
// power 'k' such that (base^k) safely fits within a u128 accumulator.