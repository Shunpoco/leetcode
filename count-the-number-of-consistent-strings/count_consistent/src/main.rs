use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn count_consistent_strings(allowed: String, words: Vec<String>) -> i32 {
        let mut hash = HashMap::new();
        
        let allowed:Vec<char> = allowed.chars().collect();
        
        for c in allowed {
            hash.insert(c, 1);
        }
        
        let mut result = 0i32;
        
        for word in words {
            let word:Vec<char> = word.chars().collect();
            let mut flag = true;
            for c in word {
                match hash.get(&c) {
                    Some(_) => continue,
                    None => {
                        flag = false;
                        break;
                    },
                }
            }
            if flag {
                result += 1;
            }
        }
        
        result
    }
}


fn main() {
    assert_eq!(Solution::count_consistent_strings("ab".to_string(), vec!["aaab".to_string(), "acdc".to_string(), "ab".to_string()]), 2);
}
