package main

func searchRange(nums []int, target int) []int {
    result := []int{-1, -1}
    search(0, len(nums), target, &nums, &result)
    
    return result
}

func search(start, end, target int, nums *[]int, result *[]int) {
    if start == end {
        return
    }
    
    m := (end+start) / 2
    
    if (*nums)[m] == target {
        if (*result)[0] == -1 || m < (*result)[0] {
            (*result)[0] = m
        }
        if (*result)[1] == -1 || m > (*result)[1] {
            (*result)[1] = m
        }
        
        search(m+1, end, target, nums, result)
        search(start, m, target, nums, result)
    } else if (*nums)[m] > target {
        search(start, m, target, nums, result)
    } else {
        search(m+1, end, target, nums, result)
    }
}
