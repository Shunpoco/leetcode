package main

import "fmt"

func convert(s string, numRows int) string {
    if numRows == 1 {
        return s
    }
    
    mod := numRows + (numRows - 2)
    result := make([][]rune, numRows)
    for i := 0; i < numRows; i++ {
        result[i] = []rune{}
    }
    
    for i, r := range s {
        m := i % mod
        if m < numRows {
            result[m] = append(result[m], r)
        } else {
            result[(numRows-1)-(m-(numRows-1))] = append(result[(numRows-1)-(m-(numRows-1))], r)
        }
    }
        
    res := ""
    for _, row := range result {
        res = fmt.Sprintf("%s%s", res, string(row))
    }
    
    return res
}
