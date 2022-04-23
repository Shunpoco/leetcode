use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        let s: Vec<char> = s.chars().collect();
        let mut memory = HashMap::new();
        
        dp(&s, 0, &mut memory)
    }
}

fn dp(s: &Vec<char>, idx: usize, memory: &mut HashMap<usize, i32>) -> i32 {
    if let Some(v) = memory.get(&idx) {
        return *v;
    }
    
    if idx == s.len() {
        return 1;
    }
    
    let mut count = 0i32;
    if valid(&s[idx..idx+1]) {
        count += dp(s, idx+1, memory);
    }
    if idx < s.len()-1 && valid(&s[idx..idx+2]) {
        count += dp(s, idx+2, memory);
    }
    
    memory.insert(idx, count);
    
    count
}

fn valid(cs: &[char]) -> bool {
    if cs.len() > 2 {
        return false;
    }
    
    if cs[0] == '0'  {
        return false;
    }

    if cs.len() == 2 {
        if cs[0] != '1' && cs[0] != '2' {
            return false;
        }
        
        if cs[0] == '2' {
            if cs[1] == '7' || cs[1] == '8' || cs[1] == '9' {
                return false;
            }
        }
    }
    
    true
}

fn main() {
    assert_eq!(Solution::num_decodings("12".to_string()), 2);
}
