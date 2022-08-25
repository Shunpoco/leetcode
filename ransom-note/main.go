package main

func canConstruct(ransomNote string, magazine string) bool {
    memory := make(map[rune]int)
    
    for _, r := range magazine {
        memory[r]++
    }
    
    for _, r := range ransomNote {
        if memory[r] <= 0 {
            return false
        }
        memory[r]--
    }
    
    return true
}
