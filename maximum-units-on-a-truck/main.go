package main

import "sort"

func maximumUnits(boxTypes [][]int, truckSize int) int {
	sort.Slice(boxTypes, func(i, j int) bool { return boxTypes[i][1] > boxTypes[j][1] })
	// fmt.Println(boxTypes)

	result := 0
	idx := 0
	for truckSize > 0 && idx < len(boxTypes) {
		var d int
		if boxTypes[idx][0] >= truckSize {
			d = truckSize
		} else {
			d = boxTypes[idx][0]
		}
		boxTypes[idx][0] -= d
		truckSize -= d

		result += boxTypes[idx][1] * d
		if boxTypes[idx][0] == 0 {
			idx++
		}
	}

	return result
}
