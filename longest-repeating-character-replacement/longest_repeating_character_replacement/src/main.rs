struct Solution;
impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let s: Vec<char> = s.chars().collect();
        let l = s.len();
        let mut lo = 0usize;
        let mut mo = 0usize;
        let mut memory = vec![0;26];
        let mut result = 0usize;
        
        for hi in 0..l {
            let v = &mut memory[s[hi] as usize - 65]; // 65 == 'A'
            *v += 1;
            mo = std::cmp::max(mo, *v);
            
            if hi-lo+1-mo > (k as usize) {
                memory[s[lo] as usize - 65] -= 1;
                lo += 1;
            }
            
            result = std::cmp::max(result, hi-lo+1);
        }
        
        result as i32
    }
}

fn main() {
    assert_eq!(Solution::character_replacement("ABAB".to_string(), 2), 4);
}
