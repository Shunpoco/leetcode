use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut dp = vec![];
        
        for &num in nums.iter() {
            if let Some(i) = dp.binary_search(&num).err() {
                if i >= dp.len() {
                    dp.push(num);
                } else {
                    dp[i] = num;
                }
            }
        }
        
        // println!("{:?}", dp);
        
        dp.len() as i32
    }
}

fn main() {
    assert_eq!(Solution::length_of_lis(vec![0,1,0,3,2,3]), 4);
}
