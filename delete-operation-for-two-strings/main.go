package main

import "sort"

func minDistance(word1 string, word2 string) int {
    l1 := len(word1)
    l2 := len(word2)
    
    memory := make([][]int, l1+1)
    for i := 0; i < l1+1; i++ {
        memory[i] = make([]int, l2+1)
    }
    
    for i := 0; i < l1+1; i++ {
        for j := 0; j < l2+1; j++ {
            var v int
            if i == 0 || j == 0 {
                v = 0
            } else if word1[i-1] != word2[j-1] {
                v = max([]int{memory[i-1][j], memory[i][j-1], memory[i-1][j-1]})
            } else {
                v = memory[i-1][j-1] + 1
            }
            
            memory[i][j] = v
        }
    }
    
    same := memory[l1][l2]
    
    return l1-same + l2-same
}

func max(nums []int) int {
    sort.Slice(nums, func(i, j int) bool { return nums[i] > nums[j] })
    return nums[0]
}
