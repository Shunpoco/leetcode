package

func removePalindromeSub(s string) int {
    if isPalindrome(s) {
        return 1
    }
    return 2
}

func isPalindrome(s string) bool {
    n := len(s)
    for i := 0; i < n/2; i++ {
        if s[i] != s[n-1-i] {
            return false
        }
    }
    
    return true
}

