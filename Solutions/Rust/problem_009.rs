// Problem 1 -
// https://projecteuler.net/problem=9
// Answer =

fn question() {
    println!("{}", {
        "
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"
    });
}

fn generate(m: i32, n: i32) -> (i32, i32, i32) {
    let a: i32 = 2 * m * n;
    let b: i32 = (m ^ 2) - (n ^ 2);
    let c: i32 = (m ^ 2) + (n ^ 2);
    return (a, b, c);
}

fn solve(num: i32) -> i32 {
    let mut m = 2;
    let mut n = 1;
    let (a, b, c) = generate(m, n);
    while a + b + c != num {
        if m == n {
            m += 1;
            n = 1;
        }
        n += 1;
        let (a, b, c) = generate(m, n);
    }
    a * b * c
}

fn main() {
    question();
    println!("The answer is {}", solve(1000));
}
