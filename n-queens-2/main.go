package main

func totalNQueens(n int) int {
    board := make([][]int, n)
    for i := 0; i < n; i++ {
        board[i] = make([]int, n)
    }
    
    result := bt(0, n, &board)
    
    return result
}

func bt(row, n int, board *[][]int) int {
    if row == n {
        return 1
    }
    
    var result int
    for col := 0; col < n; col++ {
        if check(row, col, n, board) {
            (*board)[row][col] = 1
            result += bt(row+1, n, board)
            (*board)[row][col] = 0
        }
    }
    
    return result
}

func check(row, col, n int, board *[][]int) bool {
    for i := 0; i < row; i++ {
        v := (*board)[i][col]
        if col-(row-i) >= 0 {
            v += (*board)[i][col-(row-i)]
        }
        if col+(row-i) < n {
            v += (*board)[i][col+(row-i)]
        }
        if v > 0 {
            return false
        }
    }
    
    return true
}
