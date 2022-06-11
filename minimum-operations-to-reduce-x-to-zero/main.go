package main

func minOperations(nums []int, x int) int {
    n := len(nums)
    asc := make([]int, n+1)
    dsc := make([]int, n+1)
    t_asc := 0
    t_dsc := 0
    for i := 0; i < n; i++ {
        t_asc += nums[i]
        t_dsc += nums[n-1-i]
        asc[i+1] = t_asc
        dsc[i+1] = t_dsc
    }

    result := -1
    i_asc := binarySearch(x, 0, asc)
    if i_asc <= n {
        for i_asc >= 0 {
            remain := x - asc[i_asc]
            i_dsc := binarySearch(remain, 0, dsc)

            if remain - dsc[i_dsc] == 0 && (result == -1 || result > i_asc + i_dsc) {
                result = i_asc + i_dsc
            }
            i_asc--
        }
    }
    
    return result
}


func binarySearch(x, start int, nums []int) int {
    if len(nums) == 0 {
        return start
    }
    
    m := len(nums)/2
    v := nums[m]
    if v == x {
        return start + m
    } else if v > x {
        return binarySearch(x, start, nums[:m])
    } else {
        return binarySearch(x, start+m+1, nums[m+1:])
    }
}
