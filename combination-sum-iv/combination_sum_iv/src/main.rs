use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn combination_sum4(nums: Vec<i32>, target: i32) -> i32 {
        let mut memory = HashMap::new();
        
        dp(&nums, target, &mut memory)
    }
}

fn dp(nums: &Vec<i32>, target: i32, memory: &mut HashMap<i32, i32>) -> i32 {
    if let Some(v) = memory.get(&target) {
        return *v;
    }
    
    if target < 0 {
        return -1;
    } else if target == 0 {
        return 1;
    }
    
    
    let mut count = 0i32;
    for &num in nums {
        let v = dp(nums, target-num, memory);
        if v != -1 {
            count += v;
        }
    }
    
    memory.insert(target, count);
    
    count
}


fn main() {
    assert_eq!(Solution::combination_sum4(vec![1,2,3], 4), 7);
}
