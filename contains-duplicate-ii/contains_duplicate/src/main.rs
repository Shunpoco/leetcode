use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        let mut h = HashMap::new();
        
        for (idx, num) in nums.iter().enumerate() {
            match h.get(&num) {
                None => {},
                Some(v) => {
                    if idx as i32 - *v <= k {
                        return true;
                    }
                }
            }
            h.insert(num, idx as i32);
        }
        
        false
    }
}


fn main() {
    assert_eq!(Solution::contains_nearby_duplicate(vec![1,3,1,2], 2), true)
}
