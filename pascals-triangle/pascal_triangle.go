package pascal

func generate(numRows int) [][]int {
	if numRows == 0 {
		return [][]int{}
	}
	result := make([][]int, numRows)

	temp := make([]int, 1)
	temp[0] = 1
	result[0] = temp
	for i := 1; i < numRows; i++ {
		temp = nextRow(temp)
		result[i] = temp
	}

	return result
}

func nextRow(before []int) []int {
	result := make([]int, len(before)+1)

	for i := 0; i < len(result); i++ {
		var sum int
		if i == 0 {
			sum = before[0]
		} else if i == len(before) {
			sum = before[len(before)-1]
		} else {
			sum = before[i-1] + before[i]
		}
		result[i] = sum
	}
	return result
}
