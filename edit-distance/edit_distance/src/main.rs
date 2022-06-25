struct Solution;
impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {
        let word1: Vec<char> = word1.chars().collect();
        let word2: Vec<char> = word2.chars().collect();
        let n = word1.len();
        let m = word2.len();
        
        let mut dp = vec![vec![0;m+1];n+1];
        
        for r in 0..n+1 {
            for c in 0..m+1 {
                if r == 0 {
                    dp[r][c] = c;
                } else if c == 0 {
                    dp[r][c] = r;
                } else {
                    let v = if word1[r-1] == word2[c-1] { 0 } else { 1 };
                    dp[r][c] = *[dp[r-1][c]+1, dp[r][c-1]+1, dp[r-1][c-1]+v].iter().min().unwrap();
                }
            }
        }
        
        dp[n][m] as i32
    }
}

fn main() {
    assert_eq!(Solution::min_distance("horse".to_string(), "ros".to_string()), 3);
}
