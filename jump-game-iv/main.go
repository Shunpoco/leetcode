package main

func maxResult(nums []int, k int) int {
    n := len(nums)
    dp := make([]int, n)
    for i := 0; i < n; i++ {
        dp[i] = -10000*n
    }
    
    dp[0] = nums[0]
    
    for i := 0; i < n; i++ {
        v := i+k
        if i+k >= n {
            v = n-1
        }
        for j := v; j > i; j-- {
            if nums[j] + dp[i] > dp[j] {
                dp[j] = nums[j] + dp[i]
            } else {
                break
            }
        }
    }
    
    return dp[n-1]
}
