package main

func poorPigs(buckets int, minutesToDie int, minutesToTest int) int {
    if buckets == 1 {
        return 0
    }
    
    nums := minutesToTest / minutesToDie + 1
    
    x := 1
    v := nums
    for v < buckets {
        v *= nums
        x ++
    }
    
    return x
}
