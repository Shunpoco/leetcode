use std::collections::VecDeque;

struct Solution {}

impl Solution {
    pub fn max_depth(s: String) -> i32 {
        let s_chars: Vec<char> = s.chars().collect();
        let mut stack = VecDeque::new();
        
        let mut max_depth = 0i32;
        let mut depth = 0i32;
        for c in s_chars {
            if c == '(' {
                stack.push_front(c);
                if depth > 0 {
                    depth -= 1;
                }
            } else if c == ')' {
                stack.pop_back();
                depth += 1;
            }
            
            if depth > max_depth {
                max_depth = depth;
            }
            
            if stack.len() == 0 {
                depth = 0;
            }
        }        
        max_depth
    }
}

fn main() {
    assert_eq!(Solution::max_depth("(1+(2*3)+((8)/4))+1".to_string()), 3);
}
