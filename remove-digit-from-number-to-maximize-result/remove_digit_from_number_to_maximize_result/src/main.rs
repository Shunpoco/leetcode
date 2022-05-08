struct Solution;
impl Solution {
    pub fn remove_digit(number: String, digit: char) -> String {
        let mut res = String::from("");
        let nums: Vec<char> = number.chars().collect();
        
        for (i, &n) in nums.iter().enumerate() {
            if n == digit {
                let s = format!("{}{}", &nums[..i].iter().collect::<String>(), &nums[i+1..].iter().collect::<String>());
                if s > res {
                    res = s;
                }
            }
        }
        
        res
    }
}

fn main() {
    assert_eq!(Solution::remove_digit("1231".to_string(), '1'), "231".to_string());
}
