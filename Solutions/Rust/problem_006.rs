// Problem 6 - Largest palindrome product
// https://projecteuler.net/problem=6
// Answer = 25164150

fn question() {
    println!("Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.");
}

/// Given a positive integer `num`, this function finds the difference between
/// the sum of the squares of the first `num` natural numbers and the square of
/// the sum.
/// 
/// # Arguments
/// 
/// * `num` - The positive integer for which the difference is calculated.
/// 
/// # Returns
/// 
/// The difference between the sum of the squares and the square of the sum.
/// 
/// # Examples
/// 
/// ```
/// let result = solve(10);
/// assert_eq!(result, 2640);
/// ```
/// 
/// # Time Complexity
/// 
/// The time complexity of this function is O(1)
fn solve(num: u32) -> u32 {
    //let num_range = num + 1;
    let square_of_sum: u32 = ((num * (num + 1))/2).pow(2);
    let sum_of_squares: u32 = (num * (num + 1)*((2 * num)+1))/6;
    square_of_sum - sum_of_squares
}

fn main() {
    question();
    let result = solve(100);
    println!("Answer = {}", result);
}
