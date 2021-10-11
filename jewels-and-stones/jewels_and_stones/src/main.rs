use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn num_jewels_in_stones(jewels: String, stones: String) -> i32 {
        let mut map = HashMap::new();
        
        let jewels: Vec<char> = jewels.chars().collect();
        let stones: Vec<char> = stones.chars().collect();
        
        for jewel in jewels {
            map.insert(jewel, 0usize);
        }
        
        let mut result = 0i32;
        
        for stone in stones {
            match map.get(&stone) {
                Some(_v) => {
                    result += 1;
                },
                None => {
                    continue;
                }
            }
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::num_jewels_in_stones("aA".to_string(), "aAAABBBa".to_string()), 5);
}
