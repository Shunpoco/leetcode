struct Solution {}

impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let sc: Vec<char> = s.chars().collect();
        let mut left = 0usize;
        let mut right = (sc.len() - 1) as usize;
        
        loop {
            while !sc[left].is_alphanumeric() && left < right {
                left += 1;
            }
            
            while !sc[right].is_alphanumeric() && right > left {
                right -= 1;
            }
            
            if left >= right {
                break;
            }
            
            // compare
            let l = sc[left].to_lowercase().to_string();
            let r = sc[right].to_lowercase().to_string();
            if l != r {
                return false;
            }
            
            left += 1;
            right -= 1;
        }
        
        true
    }
}

fn main() {
    assert!(Solution::is_palindrome("A man, a plan, a canal: Panama".to_string()));
}

#[test]
fn test_palindrome() {
    assert_eq!(Solution::is_palindrome("A man, a plan, a canal: Panama".to_string()), true);
    assert_eq!(Solution::is_palindrome(" ".to_string()), true);
    assert_eq!(Solution::is_palindrome("race a car".to_string()), false);
    
}
