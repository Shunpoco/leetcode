package main

func maxUncrossedLines(nums1 []int, nums2 []int) int {
    n := len(nums1)
    m := len(nums2)
    dp := make([][]int, n+1)
    
    for r := 0; r < n+1; r++ {
        dp[r] = make([]int, m+1)
        for c := 0; c < m+1; c++ {
            if r == 0 || c == 0 {
                dp[r][c] = 0
            } else {
                v := dp[r-1][c]
                if v < dp[r][c-1] {
                    v = dp[r][c-1]
                }
                if nums1[r-1] == nums2[c-1] && dp[r-1][c-1] + 1 > v{
                    v = dp[r-1][c-1] + 1
                }
                dp[r][c] = v
            }
        }
    }
    
    return dp[n][m]
}
