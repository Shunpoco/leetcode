use std::collections::HashMap;

struct Solution {}
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut h: HashMap<char, usize> = HashMap::new();
        
        let s:Vec<char> = s.chars().collect();
        
        let mut left = 0usize;
        let mut result = 0i32;
        
        for (i, c) in s.iter().enumerate() {
            match h.get(c) {
                Some(v) => {
                    if *v >= left {
                        left = *v + 1;
                    }
                },
                None => (),
            }
            h.insert(*c, i);
            
            let l = (i + 1 - left) as i32;
            if l > result {
                result = l;
            }
        }
        
        result
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
