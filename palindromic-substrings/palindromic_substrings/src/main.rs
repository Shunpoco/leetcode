struct Solution;
impl Solution {
    pub fn count_substrings(s: String) -> i32 {
        let s: Vec<char> = s.chars().collect();
        let mut result = 0i32;
        
        for right in 1..s.len()+1 {
            for left in 0..right {
                let c = &s[left..right];
                if check(c) {
                    result += 1;
                }
            }
        }
        result
    }
}

fn check(s: &[char]) -> bool {
    let n = s.len();
    
    for i in 0..n/2 {
        if s[i] != s[n-1-i] {
            return false;
        }
    }
    
    true
}


fn main() {
    assert_eq!(Solution::count_substrings("abc".to_string()), 3);
}
