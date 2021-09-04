struct Solution {}

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 || (x > 0 && x % 10 == 0){
            return false;
        }
        
        let mut mx = x;
        let mut rev = 0i32;
        
        while mx > 0 {
            match rev.checked_mul(10) {
                None => return false,
                Some(v) => rev = v,
            }
            
            match rev.checked_add(mx%10) {
                None => return false,
                Some(v) => rev = v,
            }
            
            mx = mx / 10;
        }

        rev == x
    }
}

fn main() {
    println!("{}", Solution::is_palindrome(121));
}

#[test]
fn test_is_palindrome() {
    assert_eq!(Solution::is_palindrome(121), true);
    assert_eq!(Solution::is_palindrome(0), true);
    assert_eq!(Solution::is_palindrome(-121), false);
    assert_eq!(Solution::is_palindrome(1210), false);
}
