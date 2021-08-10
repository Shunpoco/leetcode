use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let matches: HashMap<char, char> = [(']', '['), ('}', '{'), (')', '(')].iter().cloned().collect();
        
        let mut stack: Vec<char> = Vec::new();
        
        for c in s.chars() {
            let l = stack.len();
            match matches.get(&c) {
                Some(v) => {
                    if l == 0 || v != &stack[l-1] {
                        return false;
                    }
                    stack.pop();
                },
                _ => stack.push(c),
            }
        }
        
        if stack.len() > 0 {
            return false;
        }
        
        true    
    }
}

fn main() {
    Solution::is_valid("()".to_string());
}


#[test]
fn test_is_valid() {
    assert_eq!(Solution::is_valid("()".to_string()), true);
    assert_eq!(Solution::is_valid("()[]{}".to_string()), true);
    assert_eq!(Solution::is_valid("(]".to_string()), false);
    assert_eq!(Solution::is_valid("({[]})".to_string()), true);
    assert_eq!(Solution::is_valid("(".to_string()), false);
}
