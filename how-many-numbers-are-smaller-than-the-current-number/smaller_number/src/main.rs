struct Solution {}

impl Solution {
    pub fn smaller_numbers_than_current(nums: Vec<i32>) -> Vec<i32> {
        let len = nums.len();
        let mut result: Vec<i32> = vec![0; len];
        
        for i in 0..len {
            for j in i..len {
                if nums[i] > nums[j] {
                    result[i] += 1;
                } else if nums[j] > nums[i] {
                    result[j] += 1;
                }
            }
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::smaller_numbers_than_current(vec![8,0,1,2,3]), vec![4, 0, 1, 2, 3]);
}
