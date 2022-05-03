struct Solution;
impl Solution {
    pub fn find_unsorted_subarray(nums: Vec<i32>) -> i32 {
        let mut right = 0usize;
        let mut max = nums[0];
        let mut min = nums[0];
        let mut decrease = false;
        
        for i in 1..nums.len() {
            if max <= nums[i] {
                max = nums[i];
            } else {
                if !decrease {
                    decrease = true;
                    right = i;
                    min = nums[i];
                } else {
                    right = i;
                    if min > nums[i] {
                        min = nums[i];
                    }
                }
            }
        }
        
        let mut left = 0usize;
        while left < right && nums[left] <= min {
            left += 1;
        }
        
        if left == right { 0 } else { (right-left+1) as i32 }
    }
}

fn main() {
    assert_eq!(Solution::find_unsorted_subarray(vec![2,6,4,8,10,9,15]), 4);
}
