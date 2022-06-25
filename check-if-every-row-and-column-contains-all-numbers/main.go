package main

func checkValid(matrix [][]int) bool {
    n := len(matrix)
    for row := 0; row < n; row++ {
        if !validRow(row, n, &matrix) {
            return false
        }
    }
    
    for col := 0; col < n; col++ {
        if !validCol(col, n, &matrix) {
            return false
        }
    }
    
    return true
}

func validRow(row, n int, matrix *[][]int) bool {
    memory := make([]int, n)
    
    for col := 0; col < n; col++ {
        v := (*matrix)[row][col]
        if memory[v-1] == -1 {
            return false
        }
        memory[v-1] -= 1
    }
    
    return true
}

func validCol(col, n int, matrix *[][]int) bool {
    memory := make([]int, n)
    
    for row := 0; row < n; row++ {
        v := (*matrix)[row][col]
        if memory[v-1] == -1 {
            return false
        }
        memory[v-1] -= 1
    }
    
    return true
}
