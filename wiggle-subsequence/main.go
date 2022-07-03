package main

type Tuple struct {
    num int
    val int
}

func wiggleMaxLength(nums []int) int {
    n := len(nums)
    
    dp := make([][]Tuple, 2)
    dp[0] = make([]Tuple, n)
    dp[1] = make([]Tuple, n)
    dp[0][0] = Tuple{1, nums[0]}
    dp[1][0] = Tuple{1, nums[0]}
    
    for i := 1; i < n; i++ {
        // dp[0] の更新
        if dp[1][i-1].val < nums[i] {
            dp[0][i] = Tuple{dp[1][i-1].num+1, nums[i]}
        } else if dp[0][i-1].val < nums[i] {
            dp[0][i] = Tuple{dp[0][i-1].num, nums[i]}
        } else {
            dp[0][i] = Tuple{dp[0][i-1].num, dp[0][i-1].val}
        }
        
        // dp[1] の更新
        if dp[0][i-1].val > nums[i] {
            dp[1][i] = Tuple{dp[0][i-1].num+1, nums[i]}
        } else if dp[1][i-1].val > nums[i] {
            dp[1][i] = Tuple{dp[1][i-1].num, nums[i]}
        } else {
            dp[1][i] = Tuple{dp[1][i-1].num, dp[1][i-1].val}
        }
    }
    
    result := dp[0][n-1].num
    if result < dp[1][n-1].num {
        result = dp[1][n-1].num
    }
    
    return result
}
