use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut memory = HashMap::new();
        
        dp(&nums, -10001, 0, &mut memory)
    }
}

fn dp(nums: &Vec<i32>, val: i32, idx: usize, memory: &mut HashMap<usize, i32>) -> i32 {
    if let Some(v) = memory.get(&idx) {
        return *v;
    }
    
    if idx == nums.len() {
        return 0;
    }
    
    let mut count = 0i32;
    for i in idx..nums.len() {
        if val < nums[i] {
            let v = 1 + dp(nums, nums[i], i+1, memory);
            
            if v > count {
                count = v;
            }
        }
    }
    
    memory.insert(idx, count);
    
    count
}


fn main() {
    assert_eq!(Solution::length_of_lis(vec![0,1,0,3,2,3]), 4);
}
