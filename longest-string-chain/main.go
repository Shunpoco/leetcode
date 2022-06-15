package main

import "sort"

func longestStrChain(words []string) int {
    sort.Slice(words, func(i, j int) bool { return len(words[i]) < len(words[j]) })
    
    memory := make(map[int]int)
    result := chain(-1, &words, &memory)   
    
    return result
}

func chain(idx int, words *[]string, memory *map[int]int) int {
    if v, ok := (*memory)[idx+1]; ok {
        return v
    }        
    
    var result int
    for next := idx+1; next < len(*words); next++ {
        if idx == -1 || isPredecessor((*words)[idx], (*words)[next]) {
            t := 1 + chain(next, words, memory)
            if result < t {
                result = t
            }
        }
    }
    
    (*memory)[idx+1] = result
    
    return result
}

// TODO: we can use just a check (not dp)
func isPredecessor(word1, word2 string) bool {
    if len(word1)+1 != len(word2) {
        return false
    }
    
    memory := make([][]int, len(word1)+1)
    
    for i := 0; i < len(word1)+1; i++ {
        memory[i] = make([]int, len(word2)+1)
        for j := 0; j < len(word2)+1; j++ {
            if i == 0 || j == 0 {
                memory[i][j] = 0
            } else if word1[i-1] != word2[j-1] {
                memory[i][j] = max(memory[i-1][j], memory[i][j-1])
            } else {
                memory[i][j] = memory[i-1][j-1] + 1
            }
        }
    }
    
    if memory[len(word1)][len(word2)] == len(word1) {
        return true
    }
    return false
}

func max(a, b int) int {
    result := a
    if b > result {
        result = b
    }
    
    return result
}
