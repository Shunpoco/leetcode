package main

func countSegments(s string) int {
    var result int
    var count int
    for _, c := range s {
        if rune(c) == ' ' {
            if count > 0 {
                result++
            }
            count = 0
        } else {
            count++
        }
    }
    
    if count > 0 {
        result++
    }
    
    return result
}
