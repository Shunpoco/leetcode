package main

import "sort"

func sortByBits(arr []int) []int {
    memo := make(map[int][]int)

    for _, v := range arr {
        memo[count(v)] = append(memo[count(v)], v)
    }

    result := make([]int, 0, len(arr))

    for i := 0; i < 10000; i++ {
        if array, ok := memo[i]; ok {
            sort.Slice(array, func(i, j int) bool {
                return array[i] < array[j]
            })

            result = append(result, array...)
        }
    }

    return result
}

func count(v int) int {
    result := 0

    for v > 0 {
        result += v & 1
        v >>= 1
    }

    return result
}
