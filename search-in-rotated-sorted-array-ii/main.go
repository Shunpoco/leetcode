package main


func search(nums []int, target int) bool {
    for i := 0; i < len(nums); i++ {
        if nums[i] == target {
            return true
        }
        if i > 0 {
            diff := nums[i] - nums[i-1]
            if diff < 0 {
                if target > nums[i-1] || target < nums[i] {
                    return false
                }
            }
        }
    }
    
    return false
}
