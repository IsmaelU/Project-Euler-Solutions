// Problem 1- Multiples of 3 and 5
// https://projecteuler.net/problem-1
// Answer = 233168

fn question() {
    println!("Find the sum of all the multiples of 3 or 5 below 1000.")
}


fn solve(bound: i32) -> i32{
    let mut answer = 0;
        for n in 1..bound {
            if n % 3 == 0 || n % 5 == 0 {
                answer = answer + n;
            }
        }
        answer
}
    
fn main() {
    question();
    println!("{}", solve(1000));
}
