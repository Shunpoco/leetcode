struct Solution;
impl Solution {
    pub fn reverse_vowels(s: String) -> String {
        let mut s:Vec<char> = s.chars().collect();
        let mut idxs = vec![];
        let mut vowels = vec![];
        for (i, &c) in s.iter().enumerate() {
            if Self.isVowel(c) {
                idxs.push(i);
                vowels.push(c);
            }
        }
        
        for (i, &c) in vowels.iter().rev().enumerate() {
            s[idxs[i]] = c;
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
