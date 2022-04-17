struct Solution;
impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let l = nums.len();
        let mut result = vec![1;l];
        
        let (mut left, mut right) = (1, 1);
        for i in 0..nums.len() {
            result[i] *= left;
            result[l-1-i] *= right;
            left *= nums[i];
            right *= nums[l-1-i];
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::product_except_self(vec![1,2,3,4]), vec![24,12,8,6]);
}
