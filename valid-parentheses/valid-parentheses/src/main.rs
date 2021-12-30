use std::collections::HashMap;

struct Solution {}

// impl Solution {
//     pub fn is_valid(s: String) -> bool {
//         let matches: HashMap<char, char> = [(']', '['), ('}', '{'), (')', '(')].iter().cloned().collect();
        
//         let mut stack: Vec<char> = Vec::new();
        
//         for c in s.chars() {
//             let l = stack.len();
//             match matches.get(&c) {
//                 Some(v) => {
//                     if l == 0 || v != &stack[l-1] {
//                         return false;
//                     }
//                     stack.pop();
//                 },
//                 _ => stack.push(c),
//             }
//         }
        
//         if stack.len() > 0 {
//             return false;
//         }
        
//         true    
//     }
// }

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let s:Vec<char> = s.chars().collect();
        let h:HashMap<char, char> = [
            ('(', ')'),
            ('[', ']'),
            ('{', '}'),
        ].iter().cloned().collect();
        
        let mut stack: Vec<char> = vec![];
        
        for c in s {
            match h.get(&c) {
                Some(_) => {
                    stack.push(c);
                },
                None => {
                    if stack.len() == 0 {
                        return false;
                    } else {
                        let v = stack.pop().unwrap();
                        match h.get(&v) {
                            None => return false,
                            Some(v2) => {
                                if *v2 != c {
                                    return false;
                                }
                            }
                        }
                    }
                }
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
