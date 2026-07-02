// Problem 12 - Highly divisible triangular number
// https://projecteuler.net/problem=12
// Answer = 76576500

fn question() {
    println!("What is the value of the first triangle number to have over five hundred divisors?");
}

// fn count_divisors(num: u64) -> u64 {
//     if num == 1{
//         return 1
//     }
//     let limit = num.isqrt();
//     let mut count = 2;
//     for i in 2..=limit{
//         if num % i == 0{
//             count += 2;
//         }
//     }
//     if limit * limit == num{
//         count -= 1;
//     }
//     count
// }

fn count_divisors(mut num: u64) -> u64{

    let mut divisor = 2;
    let mut factors = 1;
    while divisor <= num / divisor{
        let mut exponent = 0;
        while num % divisor == 0{
            num /= divisor;
            exponent += 1
        }
        divisor += 1;
        factors *= exponent + 1;
    }
    if num > 1{
        factors *= 2
    }
    factors
}

fn find_triangle_with_divisors(target_divisors: u64) -> u64 {
    (1..).scan(0, |sum, index| {
        *sum += index;
        Some(*sum)
        }).find(|&num| count_divisors(num) > target_divisors)
        .unwrap()
}


fn main() {
    question();
    let target_divisors = 500;
    let answer = find_triangle_with_divisors(target_divisors);
    println!("The answer is {}", answer);
}