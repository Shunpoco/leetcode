package main

func minCostClimbingStairs(cost []int) int {
    n := len(cost)
    dp := make([]int, n+1)
    for i := 0; i < n+1; i++ {
        dp[i] = 100000000
    }
    dp[0] = 0
    dp[1] = 0
    
    for i := 0; i < n; i++ {
        cur := dp[i]
        cur_cost := cost[i]
        for j := 1; j < 3; j++ {
            if i+j > n {
                continue;
            }
            if dp[i+j] > cur+cur_cost {
                dp[i+j] = cur+cur_cost
            }
        }
    }
    
    return dp[n]
}
