package main

func checkPossibility(nums []int) bool {
    n := len(nums)
    count := 0
    for i := 1; i < n; i++ {
        if nums[i] < nums[i-1] {
            if count > 0 {
                return false
            }
            count++
            if i-1 == 0 || nums[i-2] <= nums[i] {
                nums[i-1] = nums[i]
            } else {
                nums[i] = nums[i-1]
            }
        }
    }

    return true
}
