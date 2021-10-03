struct Solution {}

impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut vs = vec![0; nums.len()];
        
        vs[0] = nums[0];
        
        for i in 1..nums.len() {
            vs[i] = vs[i-1] + nums[i];
        }
        
        vs
    }
}

fn main() {
    println!("{:?}", Solution::running_sum(vec![1,2,3,4,5]));
}
