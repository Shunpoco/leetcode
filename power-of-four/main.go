package main

func isPowerOfFour(n int) bool {
    count := 0
    
    for n != 0 && n&1 == 0 {
        count++
        n >>= 1
    }
    
    if count % 2 == 0 && n == 1 {
        return true
    }
    
    return false
}
