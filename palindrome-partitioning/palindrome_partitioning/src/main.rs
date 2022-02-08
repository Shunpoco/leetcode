use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn partition(s: String) -> Vec<Vec<String>> {
        let mut memory = HashMap::new();
        let s: Vec<char> = s.chars().collect();
        
        Solution::part(&s[..], &mut memory)
    }
    fn is_palindrome(s: &[char]) -> bool {
        let l = s.len();
        let m = l / 2;
        
        for i in 0..m {
            if s[i] != s[l-1-i] {
                return false;
            }
        }
        true
    }
    
    fn part(s: &[char], memory: &mut HashMap<String, Vec<Vec<String>>>) -> Vec<Vec<String>> {
        match memory.get(&s.iter().collect::<String>()) {
            Some(v) => return (*v).clone(),
            None => {},
        }
        
        let l = s.len();
        let mut result = vec![];
        
        for i in 0..l {
            let left = &s[..i+1];
            if Solution::is_palindrome(left) {
                let res = vec![left.iter().collect::<String>()];
                if left.len() == l {
                    result.push(res);
                } else {
                    let right = &s[i+1..];
                    let v = Solution::part(right, memory);
                    
                    for r in v {
                        let mut temp = res.clone();
                        temp.extend(r);
                        result.push(temp);
                    }
                }
            }
        }
        memory.insert(s.iter().collect::<String>(), result.clone());
        
        result
    }
}


fn main() {
    assert_eq!(Solution::partition(String::from("aab")), vec![vec!["a".to_string(), "a".to_string(), "b".to_string()], vec!["aa".to_string(), "b".to_string()]]);
}
