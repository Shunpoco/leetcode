struct Solution;
impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut result = vec![1;n];
        let mut left = 1i32;
        let mut right = 1i32;
        for i in 0..n {
            result[i] *= left;
            result[n-1-i] *= right;
            left *= nums[i];
            right *= nums[n-1-i];
        }
        result
    }
}

fn main() {
    assert_eq!(Solution::product_except_self(vec![1,2,3,4]), vec![24,12,8,6]);
}
