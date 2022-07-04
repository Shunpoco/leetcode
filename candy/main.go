package main

func candy(ratings []int) int {
    n := len(ratings)
    order := make([]int, n)
    reverse := make([]int, n)
    order[0] = 1
    reverse[n-1] = 1
    
    for i := 1; i < n; i++ {
        if ratings[i] > ratings[i-1] {
            order[i] = order[i-1] + 1
        } else {
            order[i] = 1
        }
        if ratings[n-1-i] > ratings[n-1-(i-1)] {
            reverse[n-1-i] = reverse[n-1-(i-1)] + 1
        } else {
            reverse[n-1-i] = 1
        }
    }
    
    fmt.Println(order, reverse)
    
    var result int
    for i := 0; i < n; i++ {
        v := order[i]
        if v < reverse[i] {
            v = reverse[i]
        }
        result += v
    }
    
    return result
}
