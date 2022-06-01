package main

func runningSum(nums []int) []int {
    result := make([]int, len(nums))
    t := 0
    for i, num := range nums {
        t += num
        result[i] = t
    }
    
    return result
}
