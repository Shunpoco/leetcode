package main

func minSetSize(arr []int) int {
    n := len(arr)
    nums := make([]int, 100001)
    
    for _, num := range arr {
        nums[num]++
    }
    sort.Slice(nums, func(i, j int) bool { return nums[i] > nums[j] })
    
    var result int
    var sum int
    for sum < n / 2 {
        sum += nums[result]
        result++
    }
    
    return result
}
