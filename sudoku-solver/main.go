func solveSudoku(board [][]byte)  {
    backtrack(0, 0, &board)
}

func backtrack(row, col int, board *[][]byte) bool {
    if row == len(*board) {
        return true
    }
    
    v := string((*board)[row][col])
    
    if v == "." {
        for _, num := range []string{"1", "2", "3", "4", "5", "6", "7", "8", "9"} {
            (*board)[row][col] = []byte(num)[0]
            if valid(row, col, board) {
                n := len(*board)
                var newRow int
                var newCol int
                if col + 1 == n {
                    newRow = row + 1
                    newCol = 0
                } else {
                    newRow = row
                    newCol = col + 1
                }
                if backtrack(newRow, newCol, board) {
                    return true
                }
            }
            (*board)[row][col] = []byte(".")[0]
        }
    } else {
        n := len(*board)
        var newRow int
        var newCol int
        if col + 1 == n {
            newRow = row + 1
            newCol = 0
        } else {
            newRow = row
            newCol = col + 1
        }
        if backtrack(newRow, newCol, board) {
            return true
        }        
    }
    
    return false
}

func valid(row, col int, board *[][]byte) bool {
    return validSubBox(row, col, board) && validRow(row, board) && validCol(col, board)
}

func validSubBox(row, col int, board *[][]byte) bool {
    candRow := []int{row, row+1, row+2}
    if row%3 == 1 {
        candRow = []int{row-1, row, row+1}
    } else if row%3 == 2 {
        candRow = []int{row-2, row-1, row}
    }
    candCol := []int{col, col+1, col+2}
    if col%3 == 1 {
        candCol = []int{col-1, col, col+1}
    } else if col%3 == 2 {
        candCol = []int{col-2, col-1, col}
    }
    
    memory := make([]int, 9)
    for _, r := range candRow {
        for _, c := range candCol {
            v := string((*board)[r][c])
            if v != "." {
                i, _ := strconv.Atoi(v)
                if memory[i-1] == -1 {
                    return false
                }
                memory[i-1]--
            }            
        }
    }
    
    return true
}

func validRow(row int, board *[][]byte) bool {
    memory := make([]int, 9)
    for c := 0; c < 9; c++ {
        v := string((*board)[row][c])
        if v != "." {
            i, _ := strconv.Atoi(v)
            if memory[i-1] == -1 {
                return false
            }
            memory[i-1]--
        }
    }
    return true
}

func validCol(col int, board *[][]byte) bool {
    memory := make([]int, 9)
    for r := 0; r < 9; r++ {
        v := string((*board)[r][col])
        if v != "." {
            i, _ := strconv.Atoi(v)
            if memory[i-1] == -1 {
                return false
            }
            memory[i-1]--
        }
    }
    return true
}

