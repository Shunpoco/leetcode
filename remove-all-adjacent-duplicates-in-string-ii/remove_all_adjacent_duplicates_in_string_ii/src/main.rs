struct Solution;
impl Solution {
    pub fn remove_duplicates(s: String, k: i32) -> String {
        let s: Vec<char> = s.chars().collect();
        let mut stack: Vec<(char, i32)> = vec![];
        
        for &c in s.iter() {
            // println!("{:?}", stack);
            if stack.len() > 0 {
                let prev = stack[stack.len()-1];
                let v:i32;
                if c == prev.0 {
                    v = prev.1+1;
                } else {
                    v = 1;
                }

                if v == k {
                    for _ in 0..(k-1) {
                        stack.pop();
                    }
                } else {
                    stack.push((c, v));
                }                
            } else {
                stack.push((c, 1));
            }
        }
        
        let mut result = vec![];
        for &(c, _) in stack.iter() {
            result.push(c);
        }
        
        result.iter().collect::<String>()
    }
}

fn main() {
    assert_eq!(Solution::remove_duplicates("deeedbbcccbdaa".to_string(), 3), "aa");
}
