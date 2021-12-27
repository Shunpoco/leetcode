struct Solution {}

// impl Solution {
//     pub fn generate_parenthesis(n: i32) -> Vec<String> {
//         if n == 0 {
//             return vec!["".to_string()];
//         }
        
//         let mut ans = vec![];
        
//         for c in 0..n {
//             for left in Solution::generate_parenthesis(c) {
//                 for right in Solution::generate_parenthesis(n-1-c) {
//                     let s = format!("{}({})", left, right);
//                     ans.push(s);
//                 }
//             }
//         }
        
//         ans
//     }
// }

// Using backtrack
impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut ans = vec![];
        
        Solution::backtrack(&mut ans, &mut vec![], n, 0, 0);
        
        ans
    }
    
    fn backtrack(ans: &mut Vec<String>, s: &mut Vec<char>, n: i32, left: i32, right: i32) {
        if s.len() == 2 * n as usize {
            ans.push(s.iter().collect());
            return
        }
        
        if left < n {
            s.push('(');
            Solution::backtrack(ans, s, n, left+1, right);
            s.pop();
        }
        
        if right < left {
            s.push(')');
            Solution::backtrack(ans, s, n, left, right+1);
            s.pop();
        }
    }
}



fn main() {
    assert_eq!(Solution::generate_parenthesis(3), vec!["((()))".to_string(),"(()())".to_string(),"()(())".to_string(),"(())()".to_string(),"()()()".to_string()])
}
