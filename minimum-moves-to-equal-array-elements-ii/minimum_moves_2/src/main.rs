struct Solution;
impl Solution {
    pub fn min_moves2(mut nums: Vec<i32>) -> i32 {
        nums.sort();
                
        let median = nums[nums.len()/2];
                
        let mut result = 0;
        for &num in nums.iter() {
            let v = num - median;
            result += if v < 0 { -v } else { v };
        }
        
        result
    }
}


fn main() {
    assert_eq!(Solution::min_moves2(vec![1,10,2,9]), 16);
}
