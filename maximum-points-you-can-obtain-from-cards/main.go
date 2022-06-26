package main

func maxScore(cardPoints []int, k int) int {
    n := len(cardPoints)
    left := make([]int, k+1)
    right := make([]int, k+1)
    
    sl := 0
    sr := 0
    for i := 0; i < k; i++ {
        sl += cardPoints[i]
        sr += cardPoints[n-1-i]
        left[i+1] = sl
        right[k+1-1-(i+1)] = sr
    }
    
    fmt.Println(left, right)
    
    result := 0
    for i := 0; i < k+1; i++ {
        v := left[i]+right[i]
        if v > result {
            result = v
        }
    }
    
    return result
}
