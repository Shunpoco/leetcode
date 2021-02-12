package pascal

func getRow(rowIndex int) []int {
	result := make([][]int, rowIndex+1)
	result[0] = []int{1}

	if rowIndex == 0 {
		return result[0]
	}

	for i := 1; i <= rowIndex; i++ {
		result[i] = create(i+1, result[i-1])
	}

	return result[rowIndex]
}

func create(idx int, before []int) []int {
	result := make([]int, idx)
	for i := 0; i < idx; i++ {
		if i == 0 {
			result[i] = before[0]
		} else if i == idx-1 {
			result[i] = before[len(before)-1]
		} else {
			result[i] = before[i-1] + before[i]
		}
	}
	return result
}
