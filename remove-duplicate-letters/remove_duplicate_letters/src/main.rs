struct Solution;
impl Solution {
    pub fn remove_duplicate_letters(s: String) -> String {
        let s: Vec<char> = s.chars().collect();
        let n = s.len();
        let mut last_occ = vec![-1;26];
        let mut visited = vec![false;26];
        let mut stack = vec![];
        
        for i in 0..n {
            last_occ[index(s[i])] = i as i32;
        }
        
        for i in 0..n {
            if !visited[index(s[i])] {
                while stack.len() > 0 && stack[stack.len()-1] > s[i] && last_occ[index(stack[stack.len()-1])] > i as i32 {
                    let v = stack.pop().unwrap();
                    visited[index(v)] = false;
                }
                stack.push(s[i]);
                visited[index(s[i])] = true;
            }
        }
        
        stack.iter().collect::<String>()
    }
}

fn index(c: char)-> usize {
    c as usize - 'a' as usize
}

fn main() {
    assert_eq!(Solution::remove_duplicate_letters("bcabc".to_string()), "abc".to_string());
}
