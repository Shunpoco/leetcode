package main

func searchMatrix(matrix [][]int, target int) bool {
    m := len(matrix)
    n := len(matrix[0])
    
    // 単純な一重ループ
    // for i := 0; i < m; i++ {
    //     if searchSlice(matrix[i], target) {
    //         return true
    //     }
    // }
    
    // 改善
    // 1. 先頭のカラムを探索して、targetよりも大きい数字を持っている行は探索から除外できる
    // 2. 末尾のカラムを探索して、targetよりも小さい数字を持っている行は探索から除外できる
    first := make([]int, m)
    last := make([]int, m)
    for i := 0; i < m; i++ {
        first[i] = matrix[i][0]
        last[i] = matrix[i][n-1]
    }
    
    b_f, r_first := searchPosition(first, target, 0)
    b_r, r_last := searchPosition(last, target, 0)
    
    // Exact matchがあったらこの時点で返す
    if b_f || b_r {
        return true
    }
    
    for i := r_last; i < r_first; i++ {
        if b, _ := searchPosition(matrix[i], target, 0); b {
            return true
        }
    }
    
    
    return false
}

func searchPosition(slice []int, target, pos int) (bool, int) {
    n := len(slice)
    if n == 0 {
        return false, pos
    }
    
    mid := n / 2
    if slice[mid] == target {
        return true, pos + mid
    } else if slice[mid] > target {
        return searchPosition(slice[:mid], target, pos)
    } else {
        return searchPosition(slice[mid+1:], target, pos+mid+1)
    }
}


// func searchSlice(slice []int, target int) bool {
//     n := len(slice)
//     if n == 0 {
//         return false
//     }
    
//     mid := n / 2
    
//     if slice[mid] == target {
//         return true
//     } else if slice[mid] > target {
//         return searchSlice(slice[:mid], target)
//     } else {
//         return searchSlice(slice[mid+1:], target)
//     }
// }
