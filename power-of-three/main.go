package main

func isPowerOfThree(n int) bool {
    if n <= 0 {
        return false
    } else if n == 1 {
        return true
    }
    
    if n % 3 == 0 {
        return isPowerOfThree(n/3)
    }
    return false
}
