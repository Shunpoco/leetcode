struct Solution {}

impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        if n == 0 {
            return vec!["".to_string()];
        }
        
        let mut ans = vec![];
        
        for c in 0..n {
            for left in Solution::generate_parenthesis(c) {
                for right in Solution::generate_parenthesis(n-1-c) {
                    let s = format!("{}({})", left, right);
                    ans.push(s);
                }
            }
        }
        
        ans
    }
}


fn main() {
    assert_eq!(Solution::generate_parenthesis(3), vec!["((()))".to_string(),"(()())".to_string(),"()(())".to_string(),"(())()".to_string(),"()()()".to_string()])
}
