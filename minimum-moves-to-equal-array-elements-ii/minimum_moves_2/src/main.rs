struct Solution;
impl Solution {
    pub fn min_moves2(mut nums: Vec<i32>) -> i32 {
        nums.sort();
        
        let m = nums.len()/2;
        let median = nums[nums.len()/2];
        
        (m as i32) * median - &nums[..m].iter().sum::<i32>() + &nums[m..].iter().sum::<i32>() - (nums.len() - m) as i32 * median
    }
}


fn main() {
    assert_eq!(Solution::min_moves2(vec![1,10,2,9]), 16);
}
