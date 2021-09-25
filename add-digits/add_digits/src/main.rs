struct Solution {}

impl Solution {
    pub fn add_digits(num: i32) -> i32 {
        if num < 10 { return num; }
        
        let mut num = num;
        let mut new_num = 0i32;
        while num > 0 {
            new_num += num % 10;
            num /= 10;
        }
        
        Solution::add_digits(new_num)
    }
}

fn main() {
    assert_eq!(Solution::add_digits(38), 2);
}

#[test]
fn test_add_digits() {
    assert_eq!(Solution::add_digits(38), 2);
    assert_eq!(Solution::add_digits(0), 0);
    assert_eq!(Solution::add_digits(4833), 9);
    assert_eq!(Solution::add_digits(4800), 3);
}
