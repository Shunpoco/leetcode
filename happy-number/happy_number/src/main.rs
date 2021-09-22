use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn is_happy(n: i32) -> bool {
        let mut h: HashMap<i32, i32> = HashMap::new();
        
        h.insert(n, 1);
        
        let mut n = n;
        
        while n > 1 {
            let mut temp = n;
            let mut val = 0i32;
            while temp > 0 {
                val += (temp % 10) * (temp % 10);
                temp = temp / 10;
            }
            
            match h.insert(val, 1) {
                None => n = val,
                Some(_) => return false,
            }
        }
        
        true
    }
}

fn main() {
    println!("Hello, world!");
}
