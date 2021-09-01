use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        
        let mut left = 0usize;
        
        let mut h: HashMap<char, usize> = HashMap::new();
        
        let mut result = 0usize;
        
        for right in 0..chars.len() {
            let c = chars[right];

            match h.get(&c) {
                None => (),
                Some(v) => {
                    if *v >= left {
                        left = *v + 1;
                    }
                }
            }

            h.insert(c, right);
            
            if right + 1 - left > result {
                result = right + 1 - left;
            }            
        }
        
        result as i32
    }
}


fn main() {
    assert_eq!(Solution::length_of_longest_substring("abcadf".to_string()), 5);
}

#[test]
fn test_length_of_longest_substring() {
    assert_eq!(Solution::length_of_longest_substring("abcabcbb".to_string()), 3);
    assert_eq!(Solution::length_of_longest_substring("bbbbb".to_string()), 1);
    assert_eq!(Solution::length_of_longest_substring("pwwkew".to_string()), 3);
    assert_eq!(Solution::length_of_longest_substring("".to_string()), 0);
}
