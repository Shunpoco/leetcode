struct Solution {}

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut result = 0i32;
        let mut last = 0i32;
        
        for c in s.chars().rev() {
            let curr = Self::get_value(c);
            if curr >= last {
                result += curr;
            } else {
                result -= curr;
            }
            last = curr;
        }
        
        result
    }
    
    fn get_value(c: char) -> i32 {
        match c {
            'I' => 1,
            'V' => 5,
            'X' => 10,
            'L' => 50,
            'C' => 100,
            'D' => 500,
            'M' => 1000,
            _ => 0,
        }
    }
}

fn main() {
    Solution::roman_to_int("IV".to_string());
}

// use std::collections::HashMap;

// impl Solution {
//     pub fn roman_to_int(s: String) -> i32 {
//         let list: HashMap<char, i32> = [('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)].iter().cloned().collect();
        
//         let mut result = 0i32;
//         let mut i = 0usize;
        
//         let chars: Vec<char> = s.chars().collect();
        
//         while i < chars.len() {
//             let mut v = list[&chars[i]];
//             if i < chars.len()-1 && v < list[&chars[i+1]] {
//                 v = list[&chars[i+1]] - v;
//                 i += 1;
//             }
//             result += v;
//             i += 1;
//         }
//         result
//     }
// }