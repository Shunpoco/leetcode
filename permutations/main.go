package main

import "fmt"

type T struct {
    array []int
    level int
}


func permute(nums []int) [][]int {
    stack := []T {T{array: []int{}, level: 0}}
    l := len(nums)    
    result := [][]int{}
    
    for len(stack) > 0 {
        n := len(stack)-1
        t := stack[n]
        stack = stack[:n]
        array := t.array
        level := t.level
        
        for _, num := range nums {
            if isin(array, num) == false {
                c := make([]int, len(array))
                copy(c, array)
                c = append(c, num)
                if len(c) == l {
                    result = append(result, c)
                } else {
                    stack = append(stack, T{array: c, level: level+1})
                }
            }
        }
        
    }
    
    return result
}

func isin(array []int, target int) bool {
    for _, num := range array {
        if target == num {
            return true
        }
    }
    
    return false
}
