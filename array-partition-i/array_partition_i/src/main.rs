struct Solution;
impl Solution {
    pub fn array_pair_sum(mut nums: Vec<i32>) -> i32 {
        nums.sort();
        
        let mut result = 0i32;
        
        for i in 0..nums.len() {
            if i%2 == 0 {
                result += nums[i];
            }
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::array_pair_sum(vec![1,4,3,2]), 4);
}
