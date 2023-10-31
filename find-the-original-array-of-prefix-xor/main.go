package main

func findArray(pref []int) []int {
    prev := 0
    result := make([]int, len(pref))

    for i, v := range pref {
        result[i] = prev^v
        prev = v
    }

    return result
}
