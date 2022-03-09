struct Solution;
impl Solution {
    pub fn reverse_words(s: String) -> String {
        let iter = s.split_ascii_whitespace();
        let mut result = "".to_string();
        let l = iter.clone().count();
        for (i, word) in iter.enumerate() {
            result.push_str(&word.chars().rev().collect::<String>());
            if i != l-1 {
                result.push_str(" ");            
            }
        }
        
        return result
    }
}


fn main() {
    assert_eq!(Solution::reverse_words("Let's take LeetCode contest".to_string()), "s'teL ekat edoCteeL tsetnoc".to_string());
}
