struct Solution {}

impl Solution {
    pub fn replace_digits(s: String) -> String {
        let mut s: Vec<char> = s.chars().collect();
        
        for i in 0..s.len() {
            if i % 2 == 1 {
                s[i] = Solution::shift(s[i-1], s[i] as u8 - 48);
            }
        }
        
        s.iter().collect()
    }
    
    fn shift(c: char, i: u8) -> char {
        (c as u8 + i) as char
    }
}


fn main() {
    assert_eq!(Solution::replace_digits("a1c1e1g".to_string()), "abcdefg".to_string())
}
