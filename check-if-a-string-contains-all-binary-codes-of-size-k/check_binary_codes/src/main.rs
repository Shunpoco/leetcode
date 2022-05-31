use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn has_all_codes(s: String, k: i32) -> bool {
        if s.len() < k as usize {
            return false;
        }
        
        let s = s.chars().collect::<Vec<_>>();
        let nums = i32::pow(2, k as u32);
        
        let mut memory = HashMap::new();
        
        for i in 0..s.len()-(k as usize -1) {
            memory.insert(s[i..i+k as usize ].iter().collect::<String>().clone(), true);
        }
        
        
        (memory.len() as i32) == nums
    }
}


fn main() {
    assert_eq!(Solution::has_all_codes(String::from("00110110"), 2), true);
}
