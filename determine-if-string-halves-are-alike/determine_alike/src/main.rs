struct Solution {}

impl Solution {
    pub fn halves_are_alike(s: String) -> bool {
        let vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
        
        let s: Vec<char> = s.chars().collect();
        let l = s.len();
        
        let mut result = 0;
        
        for i in 0..l {
            if vowels.contains(&s[i]) {
                if i < l / 2 {
                    result += 1;
                } else {
                    result -= 1;
                }
            }
        }
        
        result == 0
    }
}

fn main() {
    assert_eq!(Solution::halves_are_alike("book".to_string()), true);
}
