package main

func numsSameConsecDiff(n int, k int) []int {
    result := []int{}
    
    for i := 1; i <= 9; i++ {
        solve(i, n-1, k, &result)
    }
    
    return result
}

func solve(digit, n, k int, result *[]int) {
    if n == 0 {
        (*result) = append(*result, digit)
        return
    }
    
    v := digit % 10
    for i := 0; i <= 9; i++ {
        diff := v - i
        if diff < 0 {
            diff *= -1
        }
        if diff == k {
            solve(digit*10+i, n-1, k, result)
        }
    }
}
