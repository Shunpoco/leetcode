use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn count_k_difference(nums: Vec<i32>, k: i32) -> i32 {
        let mut hash: HashMap<i32, i32> = HashMap::new();
        
        let mut result = 0i32;
        
        for i in 0..nums.len() {
            let v = nums[i];
            let sub = k + v;
            
            let mut sub2 = 0;
            if v > k {
                sub2 = v - k;
            }
            
            match hash.get(&sub) {
                None => (),
                Some(val) => result += val,
            }
            
            if sub2 > 0 {
                match hash.get(&sub2) {
                    None => (),
                    Some(val) => result += val,
                }
            }
            
            let mut counter = 0i32;
            match hash.get(&v) {
                None => (),
                Some(val) => counter = *val,
            }
            hash.insert(v, counter+1);
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::count_k_difference(vec![1,2,2,1], 1), 4);
}
