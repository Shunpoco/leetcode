struct Solution {}

impl Solution {
    pub fn fizz_buzz(n: i32) -> Vec<String> {
        let mut result: Vec<String> = Vec::new();
        
        for i in 1..n+1 {
            let mut w = format!("{}", i);
            if i % 3 == 0 && i % 5 == 0 {
                w = "FizzBuzz".to_string();
            } else if i % 3 == 0 {
                w = "Fizz".to_string();
            } else if i % 5 == 0 {
                w = "Buzz".to_string();
            }
            result.push(w);
        }
        
        result
    }
}


fn main() {
    println!("{:?}", Solution::fizz_buzz(10));
}
