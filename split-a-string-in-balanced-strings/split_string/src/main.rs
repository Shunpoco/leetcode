struct Solution {}

impl Solution {
    pub fn balanced_string_split(s: String) -> i32 {
        let s_c: Vec<char> = s.chars().collect();
        
        let mut result = 0i32;
        
        let mut l = 0;
        let mut r = 0;
        
        for c in s_c {
            match c {
                'L' => l += 1,
                'R' => r += 1,
                _ => return result,
            }
            
            if l == r {
                result += 1;
                l = 0;
                r = 0;
            }
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::balanced_string_split("LLRRLRLR".to_string()), 3);
}


