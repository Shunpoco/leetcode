package main

func fib(n int) int {
    dp := make([]int, n+1)
    return solve(n, &dp)
    
}

func solve(n int, dp *[]int) int {
    if n == 0 || (*dp)[n] != 0 {
        return (*dp)[n]
    }
    
    var result int
    if n == 1 {
        result = 1
    } else {
        result = solve(n-1, dp) + solve(n-2, dp)    
    }
    
    (*dp)[n] = result
    
    return result
}
