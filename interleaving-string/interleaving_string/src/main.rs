// use std::collections::HashMap;

struct Solution;
// impl Solution {
//     pub fn is_interleave(s1: String, s2: String, s3: String) -> bool {
//         let (l1, l2, l3) = (s1.len(), s2.len(), s3.len());
//         if l1+l2 != l3 {
//             return false;
//         }
        
//         let s1: Vec<char> = s1.chars().collect();
//         let s2: Vec<char> = s2.chars().collect();
//         let s3: Vec<char> = s3.chars().collect();
        
//         let mut memory = HashMap::new();

//         dp(&s1, &s2, &s3, 0, 0, 0, &mut memory)
//     }
// }

// fn dp(s1: &Vec<char>, s2: &Vec<char>, s3: &Vec<char>, i1: usize, i2: usize, i3: usize, memory: &mut HashMap<(usize, usize), bool>) -> bool {
//     if let Some(v) = memory.get(&(i1, i2)) {
//         return *v;
//     }
    
//     if i3 == s3.len() {
//         return true;
//     }
    
//     let mut result = false;
//     if i1 < s1.len() && s1[i1] == s3[i3] {
//         result |= dp(s1, s2, s3, i1+1, i2, i3+1, memory);
//     }
//     if i2 < s2.len() && s2[i2] == s3[i3] {
//         result |= dp(s1, s2, s3, i1, i2+1, i3+1, memory);
//     }
    
//     memory.insert((i1, i2), result);
    
//     result
// }

// impl Solution {
//     pub fn is_interleave(s1: String, s2: String, s3: String) -> bool {
//         let (l1, l2, l3) = (s1.len(), s2.len(), s3.len());
//         if l1+l2 != l3 {
//             return false;
//         }
        
//         let s1: Vec<char> = s1.chars().collect();
//         let s2: Vec<char> = s2.chars().collect();
//         let s3: Vec<char> = s3.chars().collect();

//         let mut dp = vec![false;l2+1];
        
//         for i in 0..l1+1 {
//             for j in 0..l2+1 {
//                 if i == 0 && j == 0 {
//                     dp[j] = true;
//                 } else if i == 0 {
//                     dp[j] = dp[j-1] && s2[j-1] == s3[i+j-1];
//                 } else if j == 0 {
//                     dp[j] = dp[j] && s1[i-1] == s3[i+j-1];
//                 } else {
//                     dp[j] = (dp[j] && s1[i-1] == s3[i+j-1]) || (dp[j-1] && s2[j-1] == s3[i+j-1]);
//                 }
//             }
//         }
    
//         dp[l2]
//     }
// }

impl Solution {
    pub fn is_interleave(s1: String, s2: String, s3: String) -> bool {
        let (l1, l2, l3) = (s1.len(), s2.len(), s3.len());
        if l1+l2 != l3 {
            return false;
        }
        
        let s1: Vec<char> = s1.chars().collect();
        let s2: Vec<char> = s2.chars().collect();
        let s3: Vec<char> = s3.chars().collect();

        let mut dp = vec![vec![false;l2+1];l1+1];
        
        for i in 0..l1+1 {
            for j in 0..l2+1 {
                if i == 0 && j == 0 {
                    dp[i][j] = true;
                } else if i == 0 {
                    dp[i][j] = dp[i][j-1] && s2[j-1] == s3[i+j-1];
                } else if j == 0 {
                    dp[i][j] = dp[i-1][j] && s1[i-1] == s3[i+j-1];
                } else {
                    dp[i][j] = (dp[i][j-1] && s2[j-1] == s3[i+j-1]) || (dp[i-1][j] && s1[i-1] == s3[i+j-1]);
                }
            }
        }
        
        dp[l1][l2]
    }
}


fn main() {
    assert_eq!(Solution::is_interleave("aabcc".to_string(), "dbbca".to_string(), "aadbbcbcac".to_string()), true);
}
