package main

import "sort"

func canMakeArithmeticProgression(arr []int) bool {
    sort.Slice(arr, func(i, j int) bool { return arr[i] < arr[j] })

    diff := -1
    for i := 0; i < len(arr)-1; i ++ {
        v := arr[i+1] - arr[i]

        if diff >= 0 && v != diff {
            return false
        }

        diff = v
    }

    return true
}
