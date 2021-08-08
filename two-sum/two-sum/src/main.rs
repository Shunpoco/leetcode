use std::collections::HashMap;

struct Solution{}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut h = HashMap::new();
        
        for i in 0..nums.len() {
            let v = nums[i];
            if h.contains_key(&v) {
                return vec![h[&v] as i32, i as i32];
            }
            h.insert(target-nums[i], i);
        }
        vec![]
    }
}

fn main() {
    Solution::two_sum(vec![3,3], 6);
}

#[test]
fn test_two_sum() {
    let result = Solution::two_sum(vec![0, 1, 2], 3);
    assert_eq!(vec![1,2], result)
}
