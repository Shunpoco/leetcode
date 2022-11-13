package main

func reverseWords(s string) string {
    result := ""
    start := false
    temp := ""
    
    for _, c := range s {
        if c != ' ' {
            temp += string(c)
            start = true
        } else if start {
            if result == "" {
                result = temp
            } else {
                result = temp + " " + result
            }
            temp = ""
            start = false
        }
    }
    
    if temp != "" {
        if result == "" {
            result = temp
        } else {
            result = temp + " " + result
        }
    }
    
    return result
}
