use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let mut memory: HashMap<(usize, usize), i32> = HashMap::new();
        Self.maximize(&nums[..], 0, nums.len(), &mut memory, true)
    }
    
    fn maximize(self, nums: &[i32], start: usize, end: usize, memory: &mut HashMap<(usize, usize), i32>, s: bool) -> i32 {
        if memory.contains_key(&(start, end)) {
            return *memory.get(&(start, end)).unwrap();
        }
        
        if end-start == 0 {
            return 0;
        } else if end-start == 1 {
            return nums[start];
        } else if end-start == 2 {
            return if nums[start] > nums[start+1] { nums[start] } else { nums[start+1] };
        }
        
        let mut ans: i32;
        if s {
            let a = nums[start] + Self.maximize(&nums, start+2, end-1, memory, false);
            let b = nums[start+1] + Self.maximize(&nums, start+3, end, memory, false);
            let c = Self.maximize(&nums, start+1, end, memory, false);
            ans = if a > b { a } else { b };
            ans = if ans > c { ans } else { c };
        } else {
            let a = nums[start] + Self.maximize(&nums, start+2, end, memory, false);
            let b = nums[start+1] + Self.maximize(&nums, start+3, end, memory, false);
            ans = if a > b { a } else { b };         
        }
        
        
        memory.insert((start, end), ans);
        
        ans
    }
}


fn main() {
    assert_eq!(Solution::rob(vec![114,117,207,117,235,82,90,67,143,146,53,108,200,91,80,223,58,170,110,236,81,90,222,160,165,195,187,199,114,235,197,187,69,129,64,214,228,78,188,67,205,94,205,169,241,202,144,240]), 4077);
}
