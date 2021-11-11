struct Solution {}

impl Solution {
    pub fn max_product_difference(nums: Vec<i32>) -> i32 {
        let l = nums.len();
        
        if l < 4 {
            return 0;
        }
        let mut nums = nums;
        nums.sort();
        
        nums[l-1] * nums[l-2] - nums[1] * nums[0]
    }
}


fn main() {
    assert_eq!(Solution::max_product_difference(vec![1,2,3,4,5]), 18);
}
