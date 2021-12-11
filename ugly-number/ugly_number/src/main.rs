struct Solution {}

impl Solution {
    pub fn is_ugly(n: i32) -> bool {
        if n <= 0 {
            return false;
        }
        let mut n = n;
        
        while n > 1 {
            if n % 2 == 0 {
                n /= 2;
            } else if n % 3 == 0 {
                n /= 3;
            } else if n % 5 == 0 {
                n /= 5;
            } else {
                return false;
            }
        }
        
        true
    }
}

fn main() {
    assert_eq!(Solution::is_ugly(12), true);
}
