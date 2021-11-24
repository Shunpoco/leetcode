struct Solution {}

impl Solution {
    pub fn num_of_strings(patterns: Vec<String>, word: String) -> i32 {
        let mut result = 0;
        for pattern in patterns {
            if Solution::is_substring(pattern, &word) {
                result += 1;
            }
        }
        
        result
    }
    
    fn is_substring(sub: String, word: &str) -> bool {
        if sub.len() > word.len() {
            return false;
        }
        let sub: Vec<char> = sub.chars().collect();
        let word: Vec<char> = word.chars().collect();
        
        for i in 0..word.len()-sub.len()+1 {
            if word[i] == sub[0] {
                if word[i..i+sub.len()] == sub[0..] {
                    return true;
                }
            }
        }
        
        false
    }
}

fn main() {
    assert_eq!(Solution::num_of_strings(vec!["a".to_string(),"abc".to_string(),"bc".to_string(),"d".to_string()], "abc".to_string()), 3);
}
