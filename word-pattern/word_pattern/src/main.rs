use std::collections::HashMap;

struct Solution{}
impl Solution {
    pub fn word_pattern(pattern: String, s: String) -> bool {
        let pattern:Vec<char> = pattern.chars().collect();
        let s:Vec<_> = s.split(" ").collect();
        
        if pattern.len() != s.len() {
            return false;
        }
        
        let mut h1:HashMap<char, &str> = HashMap::new();
        let mut h2:HashMap<&str, char> = HashMap::new();
        
        for (p, w) in pattern.iter().zip(s.iter()) {            
            match h1.get(p) {
                Some(v) => {
                    if v != w {
                        return false;
                    }
                },
                None => {
                    h1.insert(*p, w);
                },
            }
            
            match h2.get(w) {
                Some(v) => {
                    if v != p {
                        return false;
                    }
                },
                None => {
                    h2.insert(w, *p);
                },
            }
        }
        
        true
    }
}


fn main() {
    assert_eq!(Solution::word_pattern("aabb".to_string(), "dog dog cat cat".to_string()), true);
}
