// impl Solution {
//     pub fn find_the_difference(s: String, t: String) -> char {
//         let mut s_chars: Vec<char> = s.chars().collect();
//         let mut t_chars: Vec<char> = t.chars().collect();
        
//         s_chars.sort_by(|a, b| b.cmp(a));
//         t_chars.sort_by(|a, b| b.cmp(a));
        
//         println!("{:?}", s_chars);
//         println!("{:?}", t_chars);
//         println!("{:?}", 'a' < 'b');   
//         s_chars[0]
//     }
// }

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn find_the_difference(s: String, t: String) -> char {
        let mut s_chars: Vec<char> = s.chars().collect();
        let mut t_chars: Vec<char> = t.chars().collect();
        
        let mut h: HashMap<char, i32> = HashMap::new();
        
        for c in s_chars {
            match h.get(&c) {
                Some(v) => {
                    h.insert(c, v+1);                
                },
                None => {
                    h.insert(c, 1);
                }
            }
        }
        
        for c in t_chars {
            match h.get(&c) {
                Some(v) => {
                    if *v == 0 {
                        return c;
                    }
                    h.insert(c, v-1);
                },
                None => {
                    return c;
                }
            }
        }
        
        ' '
    }
}


fn main() {
    println!("Hello, world!");
}
