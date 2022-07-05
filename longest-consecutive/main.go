package main

import "sort"

func longestConsecutive(nums []int) int {
    sort.Slice(nums, func(i, j int) bool { return nums[i] < nums[j] })
    
    var result int
    left := 0
    skip := 0
    for right := 0; right < len(nums); right++ {
        if right != left && nums[right]-1 != nums[right-1] {
            if nums[right] == nums[right-1] {
                skip++
            } else {           
                left = right
                skip = 0
            }
        }
        
        if right-left+1-skip > result {
            result = right-left+1-skip
        }
    }
    
    return result
}
