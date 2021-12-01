struct Solution {}

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let l = nums.len();
        let mut result = 0i32;
        
        if l == 1 {
            return result;
        }
        
        let mut prev = nums[0];
        for i in 1..l {
            let v = nums[i];
            if v <= prev {
                prev += 1;
                result += prev - v;
            } else {
                prev = v;
            }
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::min_operations(vec![1,5,2,4,1]), 14);
}
