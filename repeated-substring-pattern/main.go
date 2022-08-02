package main

func repeatedSubstringPattern(s string) bool {
    n := len(s)
    
    for l := 1; l <= n/2; l++ {
        v := s[:l]
        t := l
        for t+l <= n {
            if v != s[t:t+l] {
                break
            }
            if t+l == n {
                return true
            }
            t += l
        }        
    }
    
    return false
}
