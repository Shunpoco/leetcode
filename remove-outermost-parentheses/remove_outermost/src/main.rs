use std::collections::VecDeque;

struct Solution {}

impl Solution {
    pub fn remove_outer_parentheses(s: String) -> String {
        let mut stack = VecDeque::new();
        
        let s:Vec<char> = s.chars().collect();
        
        let mut result = "".to_string();
        let mut depth = 0usize;
        for c in s {
            stack.push_back(c);
            if c == '(' {
                depth += 1;
            } else {
                depth -= 1;
            }
            
            if depth == 0 {
                let l = stack.len();
                let mut temp = "".to_string();
                for i in 0..l {
                    match stack.pop_back() {
                        Some(v) => {
                            if i != 0 && i != l-1 {
                                temp = format!("{}{}", v, temp);
                            }
                        },
                        None => continue,
                    }
                }
                result = format!("{}{}", result, temp);
            }
            
        }
        result
    }
}

fn main() {
    assert_eq!(Solution::remove_outer_parentheses("(()())(())(()(()))".to_string()), "()()()()(())".to_string());
}
