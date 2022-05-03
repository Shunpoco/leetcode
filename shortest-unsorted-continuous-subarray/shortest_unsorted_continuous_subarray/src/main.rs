struct Solution;
impl Solution {
    pub fn find_unsorted_subarray(nums: Vec<i32>) -> i32 {
        let mut max = nums[0];
        let mut min = nums[0];
        let mut i_max = 0;
        let mut left = -1;
        let mut right = -1;
        
        for i in 1..nums.len() {
            if max < nums[i] {
                max = nums[i];
                i_max = i;
            }
            if max > nums[i] {
                if left == -1 {
                    left = i_max as i32;
                    right = i as i32;
                    min = nums[i];
                } else {
                    right = i as i32;
                    if min > nums[i] {
                        min = nums[i];
                    }
                }
            }
        }
        let mut new_left = 0i32;
        while new_left < right && nums[new_left as usize] <= min {
            new_left += 1;
        }
        
        if right == new_left { 0 } else { right-new_left+1 }
    }
}

fn main() {
    assert_eq!(Solution::find_unsorted_subarray(vec![2,6,4,8,10,9,15]), 4);
}
