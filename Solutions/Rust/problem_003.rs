// Problem 3 - Largest Prime Factor
// https://projecteuler.net/problem=3
// Answer = 6857
// Will find a better solution that doesn't need to check if number is prime by doing prime factorisation

fn question() {
    println!("What is the largest prime factor of the number 600851475143?")
}

fn is_prime(num:i64) -> bool {
    if num < 2{
        return false
    }else if num == 2{ 
        return true
    }else if num % 2 == 0 {
        return false
    }else{
        for i in (3..num.isqrt()).step_by(2){
            if num % i == 0{
                return false
            }
        } 
    }
    true
    }


fn solve(num:i64) -> i64{
    let bound = (num.isqrt()) + 1;
    let mut answer = 0;
    for i in (1..bound).rev(){
        if num % i == 0{
            if is_prime(i){
                answer = i;
                break
            }
        }
    }
    answer
}


fn main() {
    question();
    println!("Answer = {}", solve(600851475143));
}