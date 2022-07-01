package main

import "sort"

func maximumUnits(boxTypes [][]int, truckSize int) int {
    sort.Slice(boxTypes, func(i, j int) bool { return boxTypes[i][1] > boxTypes[j][1] })
    // fmt.Println(boxTypes)
    
    result := 0
    idx := 0
    for truckSize > 0 && idx < len(boxTypes) {        
        result += boxTypes[idx][1]
        boxTypes[idx][0] -= 1
        if boxTypes[idx][0] == 0 {
            idx++
        }
        truckSize--
    }
    
    return result
}
