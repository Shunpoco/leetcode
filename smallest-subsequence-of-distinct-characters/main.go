package main

func smallestSubsequence(s string) string {
    added := make([]bool, 26)
    stack := []rune{}
    lastPos := make(map[rune]int)
    for i, b := range s {
        lastPos[b] = i
    }
    
    for i, b := range s {
        if !added[int(b)-97] {
            for len(stack) > 0 && (stack[len(stack)-1] > b && lastPos[stack[len(stack)-1]] > i) {
                v := stack[len(stack)-1]
                stack = stack[:len(stack)-1]
                added[int(v)-97] = false
            }
        
            stack = append(stack, b)
            added[int(b)-97] = true   
        }
    }
    
    return string(stack)
}
