struct Solution {}

impl Solution {
    pub fn restore_string(s: String, indices: Vec<i32>) -> String {
        let s_chars: Vec<char> = s.chars().collect();
        
        let mut result = vec![' '; s_chars.len()];
        
        for i in 0..s_chars.len() {
            result[indices[i] as usize] = s_chars[i];
        }
        
        result.iter().collect()
    }
}

fn main() {
    assert_eq!(Solution::restore_string("codeleet".to_string(), vec![4,5,6,7,0,2,1,3]), "leetcode");
}
