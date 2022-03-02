struct Solution;
impl Solution {
    pub fn reverse_vowels(s: String) -> String {
        let mut s:Vec<char> = s.chars().collect();
        let mut left = 0usize;
        let mut right = s.len()-1;
        
        while left < right {
            if Self.isVowel(s[left]) && Self.isVowel(s[right]) {
                let temp = s[left];
                s[left] = s[right];
                s[right] = temp;
                left += 1;
                right -= 1;
            } else {
                if !Self.isVowel(s[left]) {
                    left += 1;
                }
                if !Self.isVowel(s[right]) {
                    right -= 1;
                }                
            }
        }

        
        s.iter().collect()
    }
    
    fn isVowel(self, c: char) -> bool {
        let list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
        if list.contains(&c) {
            return true;
        }
        false
    }
}

fn main() {
    assert_eq!(Solution::reverse_vowels("leetcode".to_string()), "leotcede".to_string());
}
