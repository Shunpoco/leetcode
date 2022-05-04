use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn max_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut memory = HashMap::new();
        
        let mut count = 0i32;
        for &num in nums.iter() {
            match memory.get_mut(&num) {
                Some(v) => {
                    if *v > 0 {
                        count += 1;
                        *v -= 1;
                    } else {
                        *memory.entry(k-num).or_insert(0) += 1;
                    }
                },
                None => {
                    *memory.entry(k-num).or_insert(0) += 1;
                }
            }
        }
        
        count
    }
}

fn main() {
    assert_eq!(Solution::max_operations(vec![1,2,3,2], 4), 2);
}
