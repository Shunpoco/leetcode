package main

func maximumUniqueSubarray(nums []int) int {
    n := len(nums)
    cums := make([]int, n+1)
    t := 0
    for i, num := range nums {
        t += num
        cums[i+1] = t
    }
    
    memory := make(map[int]int)
    result := 0
    left := 0
    for right := 0; right < n; right++ {
        if v, ok := memory[nums[right]]; ok && v >= left {
            left = v+1
        }
        memory[nums[right]] = right
        sum := cums[right+1] - cums[left]
        if sum > result {
            result = sum
        }
    }
    
    return result
}
