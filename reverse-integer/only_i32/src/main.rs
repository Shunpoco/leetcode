struct Solution {}

impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut result = 0i32;
        let mut x = x;

        while x != 0 {
            match result.checked_mul(10) {
                Some(v) => result = v,
                None => return 0,
            };
            
            match result.checked_add(x % 10) {
                Some(v) => result = v,
                None => return 0,
            };
            
            x = x / 10;
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