struct Solution {}

impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut result = 0i32;
        let mut x2 = x;
        
        while x2 != 0 {
            match result.checked_mul(10) {
                None => return 0,
                Some(v) => result = v
            }
            match result.checked_add(x2 % 10) {
                None => return 0,
                Some(v) => result = v
            }
            x2 = x2 / 10;
        }
        
        result
    }
}

fn main() {
    println!("{}", Solution::reverse(-123));
}

#[test]
fn test_reverse() {
    assert_eq!(Solution::reverse(-123), -321);
    assert_eq!(Solution::reverse(i32::MAX), 0);
    assert_eq!(Solution::reverse(i32::MIN), 0);
}