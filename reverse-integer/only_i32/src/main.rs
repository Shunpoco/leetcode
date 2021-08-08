struct Solution {}

impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut result:i32 = 0;
        let mut mx = x;
        loop {
            match result.checked_mul(10) {
                Some(v) => result = v,
                None => return 0,
            }
            
            match result.checked_add(mx%10) {
                Some(v) => result = v,
                None => return 0,
            }
            
            mx = mx / 10;
            
            if mx == 0 {
                break;
            }
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