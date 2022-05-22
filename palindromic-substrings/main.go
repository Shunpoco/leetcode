package main

func countSubstrings(s string) int {
    memory := make(map[string]bool)
    
    result := 0
    
    for w := 1; w < len(s)+1; w++ {
        for i := 0; i < len(s)-w+1; i++ {
            if isPalindrome(s[i:i+w], &memory) {
                result++
            }
        } 
    }
    
    return result
}

func isPalindrome(s string, memory *map[string]bool) bool {
    if v, prs := (*memory)[s]; prs {
        return v
    }
    
    var result bool
    if len(s) <= 1 {
        result = true
    } else if s[0] == s[len(s)-1] {
        result = isPalindrome(s[1:len(s)-1], memory)
    } else {
        result = false
    }
    
    (*memory)[s] = result
    
    return result
}
