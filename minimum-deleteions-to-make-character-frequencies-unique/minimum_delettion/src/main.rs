struct Solution;
impl Solution {
    pub fn min_deletions(s: String) -> i32 {
        let s: Vec<char> = s.chars().collect();
        
        let mut memory = vec![0;26];
        for &c in s.iter() {
            memory[(c as u8 - 'a' as u8) as usize] += 1;
        }
        
        memory.sort_by(|a, b| b.cmp(a));
        
        let mut count = 0;
        for i in 0..25 {
            for j in i+1..26 {
                if memory[i] == memory[j] && memory[i] != 0 {
                    count += 1;
                    memory[j] -= 1;
                }
            }
        }
        
        count
    }
}

fn main() {
    assert_eq!(Solution::min_deletions("aab".to_string()), 0);
}
