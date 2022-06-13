package main

type Position struct {
    Row int
    Colum int
}

func minimumTotal(triangle [][]int) int {
    memory := make(map[Position]int)
    
    return solve(0, 0, &triangle, &memory)
}

func solve(row, column int, triangle *[][]int, memory *map[Position]int) int {
    if v, ok := (*memory)[Position{row, column}]; ok {
        return v
    }
    
    v := (*triangle)[row][column]
    result := v
    if row+1 < len(*triangle) {
        modify := false
        n := len((*triangle)[row+1])
        for i := 0; i < 2; i++ {
            if column+i < n {
                t := v + solve(row+1, column+i, triangle, memory)
                if !modify || result > t {
                    result = t
                    modify = true
                }
            }
        }        
    }
    
    (*memory)[Position{row, column}] = result
    
    return result
}
