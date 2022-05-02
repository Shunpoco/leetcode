struct Solution;
impl Solution {
    pub fn backspace_compare(s: String, t: String) -> bool {
        let s: Vec<char> = s.chars().collect();
        let t: Vec<char> = t.chars().collect();
        
        let mut stack = vec![];
        for &c in s.iter() {
            if c == '#' {
                if stack.len() > 0 {
                    stack.pop();                
                }
            } else {
                stack.push(c);
            }
        }
        
        let mut stack2 = vec![];
        for &c in t.iter() {
            if c == '#' {
                if stack2.len() > 0 {
                    stack2.pop();
                }
            } else {
                stack2.push(c);
            }
        }
        
        stack == stack2
    }
}


fn main() {
    assert_eq!(Solution::backspace_compare("a##b".to_string(), "b".to_string()), true);
}
