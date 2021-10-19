struct Solution {}

impl Solution {
    pub fn interpret(command: String) -> String {
        let c_chars: Vec<char> = command.chars().collect();
        
        let mut result = String::from("");
        
        let mut prev = '\0';
        
        for c in c_chars {
            if c == 'G' {
                result.push('G');
            } else if c == ')' && prev == '(' {
                result.push('o');
            } else if c == ')' && prev == 'l' {
                result.push_str("al");
            }
            
            prev = c
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::interpret("G()(al)".to_string()), "Goal".to_string());
}
