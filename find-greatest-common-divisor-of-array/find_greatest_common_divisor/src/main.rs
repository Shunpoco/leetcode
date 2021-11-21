struct Solution {}

impl Solution {
    pub fn find_gcd(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        nums.sort();
        
        let (mut min, mut max) = (nums[0], nums[nums.len()-1]);
        
        let mut r = max % min;
        
        while r != 0 {
            max = min;
            min = r;
            r = max % min;            
        }
        
        min
    }
}

fn main() {
    assert_eq!(Solution::find_gcd(vec![2,5,6,9,10]), 2);
}
