package main

func numSquares(n int) int {
    memory := make(map[int]int)
    return exec(n, &memory)
}

func exec(n int, memory *map[int]int) int {
    if n <= 1 {
        return n
    }
    
    if v, ok := (*memory)[n]; ok {
        return v
    }
    
    result := n
    for num := 1; num*num <= n; num++ {
        t := n/(num*num) 
        t += exec(n-num*num*t, memory)
        
        if t < result {
            result = t
        }
    }
    
    (*memory)[n] = result
    return result
}
