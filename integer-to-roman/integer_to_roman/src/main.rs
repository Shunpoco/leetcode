struct Solution;

impl Solution {
    pub fn int_to_roman(num: i32) -> String {
        let pairs = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")];
        
        let mut num = num;
        let mut result = String::from("");
        
        for (n, r) in &pairs {
            let v = num / n;
            if v > 0 {
                for _ in 0..(v as usize) {
                    result = format!("{}{}", result, r);
                }
                num %= n;
                if num == 0 {
                    break;
                }
            }                
        }
        
        result
    }
}


fn main() {
    assert_eq!(Solution::int_to_roman(3), "III".to_string());
}
