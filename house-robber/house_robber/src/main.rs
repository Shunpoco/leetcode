use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let mut memory: HashMap<usize, i32> = HashMap::new();
        Self.maximize(&nums[..], &mut memory)
    }
    
    fn maximize(self, nums: &[i32], memory: &mut HashMap<usize, i32>) -> i32 {
        if memory.contains_key(&nums.len()) {
            return *memory.get(&nums.len()).unwrap();
        }
        
        if nums.len() == 0 {
            return 0;
        } else if nums.len() == 1 {
            return nums[0];
        } else if nums.len() == 2 {
            return if nums[0] > nums[1] { nums[0] } else { nums[1] };
        }
        
        let a = nums[0] + Self.maximize(&nums[2..], memory);
        let b = nums[1] + Self.maximize(&nums[3..], memory);
        
        let ans =  if a > b { a } else { b };
        
        memory.insert(nums.len(), ans);
        
        ans
    }
}


fn main() {
    assert_eq!(Solution::rob(vec![82,217,170,215,153,55,185,55,185,232,69,131,130,102]), 1082);
}
