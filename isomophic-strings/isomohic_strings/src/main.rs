use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        let mut h1: HashMap<char, char> = HashMap::new();
        let mut h2: HashMap<char, char> = HashMap::new();
        
        let s = s.chars();
        let t = t.chars();
        
        for (cs, ct) in s.zip(t) {            
            match h1.get(&cs) {
                Some(v) => {
                    if *v != ct {
                        return false;
                    }
                },
                None => {h1.insert(cs, ct);},
            }
            
            match h2.get(&ct) {
                Some(v) => {
                    if *v != cs {
                        return false;
                    }
                },
                None => {h2.insert(ct, cs);},
            }
        }
        
        true
    }
}


fn main() {
    assert_eq!(Solution::is_isomorphic("egg".to_string(), "add".to_string()), true);
}
