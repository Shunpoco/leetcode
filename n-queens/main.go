package main

func solveNQueens(n int) [][]string {
    cur := make([][]string, n)
    for r := 0; r < n; r++ {
        t := make([]string, n)
        for c := 0; c < n; c++ {
            t[c] = "."
        }
        cur[r] = t
    }

    res := [][]string{}
    
    bt(0, n, &cur, &res)
    
    return res
}

func bt(r, n int, cur *[][]string, res *[][]string) bool {
    if r == n {
        result := make([]string, n)
        for i, c := range (*cur) {
            t := ""
            for _, v := range c {
                t += v
            }
            result[i] = t
        }
        (*res) = append((*res), result)
        return true
    }
    
    
    for i := 0; i < n; i++ {
        if check(r, i, cur) {
            (*cur)[r][i] = "Q"
            bt(r+1, n, cur, res)
            (*cur)[r][i] = "."            
        }
    }
    
    return false
}

func check(r, c int, cur *[][]string) bool {
    for i := 0; i < r; i++ {
        if (*cur)[i][c] == "Q" {
            return false
        } 
        if c-(r-i) >= 0 && (*cur)[i][c-(r-i)] == "Q" {
            return false
        }
        if c+(r-i) < len(*cur) && (*cur)[i][c+(r-i)] == "Q" {
            return false
        }
    }
    
    return true
}
