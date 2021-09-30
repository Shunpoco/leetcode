struct Solution {}

impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut ans = vec![0i32; n*2];
        
        for i in 0..n {
            ans[i] = nums[i];
            ans[i+n] = nums[i];
        }
        
        ans
    }
}

fn main() {
    println!("{:?}", Solution::get_concatenation(vec![1,2,3]));
}
