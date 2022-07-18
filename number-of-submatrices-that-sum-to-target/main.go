package main

func numSubmatrixSumTarget(matrix [][]int, target int) int {
    m := len(matrix)
    n := len(matrix[0])
    mem := make([][]int, m)
    for i := 0; i < m; i++ {
        mem[i] = make([]int, n+1)
        prev := 0
        for j := 1; j < n+1; j++ {
            mem[i][j] = matrix[i][j-1] + prev
            prev = mem[i][j]
        }
    }
    
    var result int
    for cs := 0; cs < n; cs++ {
        for es := cs+1; es < n+1; es++ {
            for rs := 0; rs < m; rs++ {
                var t int
                for re := rs; re < m; re++ {
                    t += mem[re][es] - mem[re][cs]
                    
                    if t == target {
                        result++
                    }
                }
            }
        }
    }
    
    return result
}
