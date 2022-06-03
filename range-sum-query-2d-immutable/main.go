package main

type NumMatrix struct {
    Cums [][]int
}


func Constructor(matrix [][]int) NumMatrix {
    nrow := len(matrix)
    ncol := len(matrix[0])
    
    cums := make([][]int, nrow)
    for i:=0; i<nrow; i++ {
        cum := make([]int, ncol+1)
        c := 0
        for j, v := range matrix[i] {
            c += v
            cum[j+1] = c
        }
        cums[i] = cum
    }
    
    return NumMatrix{
        Cums: cums,
    }    
}


func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
    result := 0
    for i := row1; i < row2+1; i++ {
        result += this.Cums[i][col2+1] - this.Cums[i][col1]
    }
    
    return result
}

