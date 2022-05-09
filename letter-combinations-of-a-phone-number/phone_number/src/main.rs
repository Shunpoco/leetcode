use std::collections::HashMap;

struct Solution;
// impl Solution {
//     pub fn letter_combinations(digits: String) -> Vec<String> {
//         if digits == String::from("") {
//             return vec![];
//         }
//         let h: HashMap<char, String> = [
//             ('2', String::from("abc")),
//             ('3', String::from("def")),
//             ('4', String::from("ghi")),
//             ('5', String::from("jkl")),
//             ('6', String::from("mno")),
//             ('7', String::from("pqrs")),
//             ('8', String::from("tuv")),
//             ('9', String::from("wxyz")),
//         ].iter().cloned().collect();

//         let digits = digits.chars();
//         let mut result: Vec<String> = vec![String::from("")];
        
//         for d in digits {
//             let pairs = h.get(&d).unwrap().chars();
//             let mut temp: Vec<String> = Vec::new();
            
//             for p in pairs {
//                 for s in &result {
//                     temp.push(format!("{}{}", s, p));
//                 }
//             }
            
//             result = temp;
//         }
        
//         result
//     }
// }

impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        let mut digits: Vec<char> = digits.chars().collect();
        
        if digits.len() == 0 {
            return vec![];
        }
        
        let mut table = HashMap::from([
            ('2', Vec::from(['a', 'b', 'c'])),
            ('3', Vec::from(['d', 'e', 'f'])),
            ('4', Vec::from(['g', 'h', 'i'])),
            ('5', Vec::from(['j', 'k', 'l'])),
            ('6', Vec::from(['m', 'n', 'o'])),
            ('7', Vec::from(['p', 'q', 'r', 's'])),
            ('8', Vec::from(['t', 'u', 'v'])),
            ('9', Vec::from(['w', 'x', 'y', 'z'])),
        ]);
        
        let mut stack = vec![vec![];1];
        let mut result = vec![];
        let l = digits.len();
        while stack.len() > 0 {
            let t = stack.pop().unwrap();
            if t.len() == l {
                result.push(t.iter().collect::<String>());
                continue;
            }
            let digit = digits[t.len()];
            for &d in table.get(&digit).unwrap() {
                let mut t_ = t.clone();
                t_.push(d);
                stack.push(t_);
            }            
        }
        
        result
    }
}



fn main() {
    assert_eq!(Solution::letter_combinations(String::from("2")), vec![String::from("a"), String::from("b"), String::from("c")])
}
