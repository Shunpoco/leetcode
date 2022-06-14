package main

func longestCommonSubsequence(text1 string, text2 string) int {
    l1 := len(text1)
    l2 := len(text2)
    memory := make([][]int, l1+1)
    for i:=0; i<l1+1; i++ {
        memory[i] = make([]int, l2+1)
        for j:=0; j<l2+1; j++ {
            var v int
            if i == 0 || j == 0 {
                v = 0
            } else if text1[i-1] != text2[j-1] {
                v = max(memory[i][j-1], memory[i-1][j], memory[i-1][j-1])
            } else {
                v = memory[i-1][j-1] + 1
            }
            
            memory[i][j] = v
        }
    }
    
    return memory[l1][l2]
}

func max(num1, num2, num3 int) int {
    m := num1
    if num2 > m {
        m = num2
    }
    if num3 > m {
        m = num3
    }
    
    return m
}
