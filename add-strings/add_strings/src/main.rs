struct Solution;
impl Solution {
    pub fn add_strings(num1: String, num2: String) -> String {
        let num1: Vec<char> = num1.chars().collect();
        let num2: Vec<char> = num2.chars().collect();
        
        let mut len = num1.len();
        if num2.len() > len {
            len = num2.len();
        }
        
        let mut idx = 0usize;
        let mut result = vec![];
        let mut carry = 0u32;
        while idx < len {
            let v1 = if idx < num1.len() { num1[num1.len()-1-idx].to_digit(10).unwrap() } else { 0 };
            let v2 = if idx < num2.len() { num2[num2.len()-1-idx].to_digit(10).unwrap() } else { 0 };
            let mut v = carry + v1 + v2;
            if v > 9 {
                carry = 1;
                v %= 10;
            } else {
                carry = 0;
            }
            result.push(char::from_digit(v, 10).unwrap());
            idx += 1;
        }
        
        if carry == 1 {
            result.push(char::from_digit(carry, 10).unwrap());
        }
        
        let s: String = result.iter().rev().collect();
        s
    }
}

fn main() {
    assert_eq!(Solution::add_strings("111".to_string(), "111".to_string()), "222".to_string());
}
