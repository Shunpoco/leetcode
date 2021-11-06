use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn longest_palindrome(s: String) -> i32 {
        let mut hash: HashMap<char, i32> = HashMap::new();
        let s: Vec<char> = s.chars().collect();
        
        for c in s {
            match hash.get(&c) {
                Some(v) => {
                    hash.insert(c, *v+1);
                },
                None => {
                    hash.insert(c, 1);
                },
            }
        }
        
        let mut result = 0i32;
        let mut use_1 = false;
        
        for (_key, value) in &hash {
            if value % 2 == 0 {
                result += value;
            } else if !use_1 {
                result += value;
                use_1 = true;
            } else {
                result += value - 1;
            }
        }
        result
    }
}

fn main() {
    assert_eq!(Solution::longest_palindrome("bananas".to_string()), 5);
}
