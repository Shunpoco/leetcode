struct Solution {}

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 || (x != 0 && x % 10 == 0){
            return false;
        }
        
        let mut rev = 0i32;
        let mut mx = x;
        
        while mx > 0 {
            match rev.checked_mul(10) {
                Some(v) => rev = v,
                None => return false,
            }
            match rev.checked_add(mx%10) {
                Some(v) => rev = v,
                None => return false,
            }
            mx = mx / 10;            
        }
        
        x == rev
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
