package main

type RowColumn struct {
    Row int
    Column int
}

func numIslands(grid [][]byte) int {
    m := len(grid)
    n := len(grid[0])
    result := 0
    arrived := make([][]bool, m)
    for i := 0; i < m; i++ {
        arrived[i] = make([]bool, n)
    }
    
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == '1' && !arrived[i][j] {
                result++
                queue := []RowColumn{{i, j}}
                arrived[i][j] = true
                for len(queue) > 0 {
                    v := queue[0]
                    queue = queue[1:]
                    if grid[v.Row][v.Column] == '1' {
                        if v.Row > 0 && !arrived[v.Row-1][v.Column] {
                            arrived[v.Row-1][v.Column] = true
                            queue = append(queue, RowColumn{v.Row-1, v.Column})
                        }
                        if v.Row < m-1 && !arrived[v.Row+1][v.Column] {
                            arrived[v.Row+1][v.Column] = true
                            queue = append(queue, RowColumn{v.Row+1, v.Column})
                        }
                        if v.Column > 0 && !arrived[v.Row][v.Column-1] {
                            arrived[v.Row][v.Column-1] = true
                            queue = append(queue, RowColumn{v.Row, v.Column-1})
                        }
                        if v.Column < n-1 && !arrived[v.Row][v.Column+1] {
                            arrived[v.Row][v.Column+1] = true
                            queue = append(queue, RowColumn{v.Row, v.Column+1})
                        }                        
                    }
                }
            }
        }
    }
    
    return result
}
