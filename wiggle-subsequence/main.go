package main

func wiggleMaxLength(nums []int) int {
	result := []int{}
	isIncrease := true

	for i, num := range nums {
		if i == 0 {
			result = append(result, num)
		} else if len(result) == 1 {
			if num > result[0] {
				isIncrease = false
				result = append(result, num)
			} else if num < result[0] {
				isIncrease = true
				result = append(result, num)
			}
		} else {
			if isIncrease {
				if num > result[len(result)-1] {
					isIncrease = false
					result = append(result, num)
				} else if num < result[len(result)-1] {
					result[len(result)-1] = num
				}
			} else {
				if num < result[len(result)-1] {
					isIncrease = true
					result = append(result, num)
				} else if num > result[len(result)-1] {
					result[len(result)-1] = num
				}
			}
		}
	}

	return len(result)
}
