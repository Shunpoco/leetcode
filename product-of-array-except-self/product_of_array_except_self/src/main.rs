use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut result = vec![];
        let mut memory = HashMap::new();
        memory.insert(nums.len(), 1);
        
        let mut v = 1i32;
        for i in 0..nums.len() {
            result.push(v*exec(&nums, i+1, &mut memory));
            v *= nums[i];
        }
        
        result        
    }
}

fn exec(nums: &Vec<i32>, idx: usize, memory: &mut HashMap<usize, i32>) -> i32 {
    if let Some(v) = memory.get(&idx) {
        return *v;
    }
    let result:i32;
    if idx == nums.len()-1 {
        result = nums[idx];
    } else {
        result = nums[idx] * exec(nums, idx+1, memory);
    }
    
    memory.insert(idx, result);
    
    result
}

fn main() {
    assert_eq!(Solution::product_except_self(vec![1,2,3,4]), vec![24,12,8,6]);
}
