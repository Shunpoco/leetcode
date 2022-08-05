package main

func combinationSum4(nums []int, target int) int {
    dp := make([]int, target+1)
    for i := 0; i < target+1; i++ {
        if i == 0 {
            dp[i] = 1
        } else {
            dp[i] = -1
        }
    }
    
    result := solve(&nums, target, &dp)
    
    return result
}

func solve(nums *[]int, target int, dp *[]int) int {
    if target < 0 {
        return 0
    }
    if v := (*dp)[target]; v != -1 {
        return v
    }
    
    result := 0
    for i := 0; i < len(*nums); i++ {
        result += solve(nums, target - (*nums)[i], dp)
    }

    (*dp)[target] = result
    
    return result
}
