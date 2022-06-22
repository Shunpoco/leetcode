use std::collections::HashMap;
use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    pub fn frequency_sort(s: String) -> String {
        let s: Vec<char> = s.chars().collect();
        let mut hm = HashMap::new();
        for &c in s.iter() {
            *hm.entry(c).or_insert(0) += 1; 
        }
        
        let mut bp = BinaryHeap::new();
        for (&key, &value) in hm.iter() {
            bp.push((value, key));
        }
        
        let mut result = String::from("");
        while bp.len() > 0 {
            let (v, c) = bp.pop().unwrap();
            result = format!("{}{}", result, vec![c;v].iter().collect::<String>());
        }
        
        result
    }
}


fn main() {
    assert_eq!(Solution::frequency_sort("tree".to_string()), "eetr".to_string());
}
