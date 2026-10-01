struct Solution;
impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let s: Vec<char> = s.chars().collect();

        let mut l = 0;
        let mut r = s.len()-1;

        while l < r {
            while l < r && !s[l].is_alphanumeric() {
                l += 1;
            }
            while r > l && !s[r].is_alphanumeric() {
                r -= 1;
            }

            if s[l].to_lowercase().to_string() != s[r].to_lowercase().to_string() {
                return false;
            }

            if l == r {
                return true;
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
        let s = "A man, a plan, a canal: Panama".to_string();
        assert!(Solution::is_palindrome(s));
    }

    #[test]
    fn second() {
        let s = "race a car".to_string();
        assert!(!Solution::is_palindrome(s));
    }

    #[test]
    fn third() {
        let s = " ".to_string();
        assert!(Solution::is_palindrome(s));
    }

    #[test]
    fn forth() {
        let s = "a.".to_string();
        assert!(Solution::is_palindrome(s));
    }
}
