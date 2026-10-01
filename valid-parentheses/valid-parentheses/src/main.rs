use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn is_valid(s: String) -> bool {
        let pairs = HashMap::from([
            (')', '('),
            (']', '['),
            ('}', '{'),
        ]);

        let mut stack = vec![];

        for c in s.chars().collect::<Vec<char>>() {
            match c {
                '(' | '[' | '{' => stack.push(c),
                ')' | ']' | '}' => {
                    if stack.len() == 0 {
                        return false;
                    }

                    let l = stack.pop().unwrap();

                    let v = *pairs.get(&c).unwrap();

                    if l != v {
                        return false;
                    }
                },
                _ => return false,
            } 
        }

        stack.len() == 0
    }
}

fn main() {
    let s = format!("()");
    let r = Solution::is_valid(s);

    println!("{r}");
}


#[test]
fn test_is_valid() {
    assert!(Solution::is_valid("()".to_string()));
    assert!(Solution::is_valid("()[]{}".to_string()));
    assert!(!Solution::is_valid("(]".to_string()));
    assert!(Solution::is_valid("([])".to_string()));
    assert!(!Solution::is_valid("([)]".to_string()));
}