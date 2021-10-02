use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn final_value_after_operations(operations: Vec<String>) -> i32 {
        let map: HashMap<&str, i32> = [
            ("X++", 1),
            ("++X", 1),
            ("X--", -1),
            ("--X", -1),
        ].iter().cloned().collect();
        
        let mut result = 0i32;
        
        for s in operations {
            let v = map.get(s.as_str()).unwrap();
            result += v;
        }
        
        result
    }
}

fn main() {
    println!("{}", Solution::final_value_after_operations(vec!["X++".to_string(), "--X".to_string()]));
}
