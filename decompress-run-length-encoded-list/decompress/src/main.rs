struct Solution {}

impl Solution {
    pub fn decompress_rl_elist(nums: Vec<i32>) -> Vec<i32> {
        let mut result: Vec<i32> = vec![];
        
        for i in 0..(nums.len() / 2) {
            let freq = nums[2*i];
            let val = nums[2*i+1];
            
            for _j in 0..freq {
                result.push(val);
            }
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::decompress_rl_elist(vec![1,2,3,4]), vec![2,4,4,4]);
}
