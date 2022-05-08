struct Solution;
impl Solution {
    pub fn count_prefixes(words: Vec<String>, s: String) -> i32 {
        let words: Vec<Vec<char>> = words.iter().map(|x| x.chars().collect::<Vec<char>>()).collect();
        let s: Vec<char> = s.chars().collect();
        
        let mut count = 0i32;
        for word in words {
            let mut idx = 0usize;
            let mut pref = true;
            for c in word {
                if idx == s.len() {
                    pref = false;
                    break;
                }
                if c == s[idx] {
                    idx += 1;
                } else {
                    pref = false;
                    break;
                }
            }
            if pref {
                count += 1;
            }
        }
        
        count
    }
}

fn main() {
    assert_eq!(Solution::count_prefixes(vec!["abc".to_string(), "a".to_string()], "ac".to_string()), 1);
}
