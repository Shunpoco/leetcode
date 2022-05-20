package main

type pos struct {
    x int
    y int
}

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    memory := make(map[pos]int)
    
    return dp(0, 0, len(obstacleGrid), len(obstacleGrid[0]), &obstacleGrid, &memory)
}

func dp(x, y, m, n int, grid *[][]int, memory *map[pos]int) int {
    if v, prs := (*memory)[pos{x, y}]; prs {
        return v
    }
    
    if x == m-1 && y == n-1 && (*grid)[x][y] == 0 {
        return 1
    }
    
    var result int
    if (*grid)[x][y] == 1 {
        result = 0
    } else {
        if x+1 < m {
            result += dp(x+1, y, m, n, grid, memory)        
        }
        if y+1 < n {
            result += dp(x, y+1, m, n, grid, memory)        
        }
    }
    
    (*memory)[pos{x, y}] = result
    
    return result
}
