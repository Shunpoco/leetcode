struct Solution;
impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        }

        // Measure x's digits.
        let mut y = x;
        let mut digit = 1;
        while y > 0 {
            if y / 10 > 0 {
                digit += 1;
            }
            y /= 10;
        }

        let x = x as i64;

        let mut l = 1;
        let mut r = digit-1;
        while r >= l {
            // The first digit.
            let a = x % ((10 as i64).pow(l)) / ((10 as i64).pow(l-1));
            // The largest digit.
            let b = x % ((10 as i64).pow(r+1)) / ((10 as i64).pow(r));

            if a != b {
                return false;
            }

            l += 1;
            r -= 1;
        }

        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn first() {
        assert!(Solution::is_palindrome(121));
    }

    #[test]
    fn second() {
        assert!(!Solution::is_palindrome(-121));
    }

    #[test]
    fn third() {
        assert!(!Solution::is_palindrome(10));
    }

    #[test]
    fn forth() {
        assert!(!Solution::is_palindrome(1000021));
    }

    #[test]
    fn fifth() {
        assert!(Solution::is_palindrome(1410110141));
    }
}