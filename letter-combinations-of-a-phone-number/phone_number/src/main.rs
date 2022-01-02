use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        if digits == String::from("") {
            return vec![];
        }
        let h: HashMap<char, String> = [
            ('2', String::from("abc")),
            ('3', String::from("def")),
            ('4', String::from("ghi")),
            ('5', String::from("jkl")),
            ('6', String::from("mno")),
            ('7', String::from("pqrs")),
            ('8', String::from("tuv")),
            ('9', String::from("wxyz")),
        ].iter().cloned().collect();

        let digits = digits.chars();
        let mut result: Vec<String> = vec![String::from("")];
        
        for d in digits {
            let pairs = h.get(&d).unwrap().chars();
            let mut temp: Vec<String> = Vec::new();
            
            for p in pairs {
                for s in &result {
                    temp.push(format!("{}{}", s, p));
                }
            }
            
            result = temp;
        }
        
        result
    }
}


fn main() {
    assert_eq!(Solution::letter_combinations(String::from("2")), vec![String::from("a"), String::from("b"), String::from("c")])
}
