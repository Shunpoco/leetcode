struct Solution {}

impl Solution {
    pub fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
        let max = candies.iter().max().unwrap();
        let mut result = vec![false; candies.len()];
        
        for i in 0..candies.len() {
            if candies[i] + extra_candies >= *max {
                result[i] = true;
            }
        }
        
        result
    }
}

fn main() {
    println!("{:?}", Solution::kids_with_candies(vec![1,2,3], 3));
}
