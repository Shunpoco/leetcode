package main

type Pos struct {
    x int
    y int
}

func shortestPathBinaryMatrix(grid [][]int) int {
    n := len(grid)
    
    queue := make([]Pos, n*n)
    score := make([][]int, n)
    for i := 0; i < n; i++ {
        score[i] = make([]int, n)
    }
    score[0][0] = 1
    
    // fmt.Println(score)
    
    for len(queue) > 0 {
        pos := queue[0]
        queue = queue[1:]
        
        if grid[pos.x][pos.y] == 1 {
            score[pos.x][pos.y] = -1
            continue
        }
        
        v := score[pos.x][pos.y]
        
        for _, i := range []int{-1, 0, 1} {
            for _, j := range []int{-1, 0, 1} {
                if pos.x+i >= 0 && pos.x+i < n && pos.y+j >= 0 && pos.y+j < n {
                    if score[pos.x+i][pos.y+j] == -1 {
                        continue
                    }
                    
                    if score[pos.x+i][pos.y+j] == 0 || score[pos.x+i][pos.y+j] > v+1 {
                        score[pos.x+i][pos.y+j] = v+1
                        queue = append(queue, Pos{pos.x+i, pos.y+j})
                    }
                }
            }
        }
        
    }
    
    r := score[n-1][n-1]
    if r == 0 {
        return -1
    }
    return r
}
