packaged main

func missingNumber(nums []int) int {
    has := make([]int, len(nums)+1)
    
    for _, num := range nums {
        has[num] = 1
    }
    for i, v := range has {
        if v == 0 {
            return i
        }
    }
    
    return 0
}
