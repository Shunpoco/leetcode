use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn can_construct(ransom_note: String, magazine: String) -> bool {
        let mut h: HashMap<char, i32> = HashMap::new();
        
        let c_ransom: Vec<char> = ransom_note.chars().collect();
        let c_magazine: Vec<char> = magazine.chars().collect();
        
        for c in c_magazine {
            match h.get(&c) {
                Some(v) => {
                    h.insert(c, v+1);
                },
                None => {
                    h.insert(c, 1);
                }
            }
        }
        
        for c in c_ransom {
            match h.get(&c) {
                None => {
                    return false;
                },
                Some(v) => {
                    if *v == 0 {
                        return false;
                    }
                    h.insert(c, v-1);
                }
            }
        }
        
        true
    }
}

fn main() {
    println!("{}", Solution::can_construct("aa".to_string(), "aab".to_string()));
}
