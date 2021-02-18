package twosum

func twoSum(numbers []int, target int) []int {
	i1 := 0
	i2 := 0
	for idx, val := range numbers {
		temp := target - val
		i2 = binarySearch(numbers[idx+1:], temp, 0)
		if i2 >= 0 {
			i1 = idx + 1
			i2 += idx + 2
			return []int{i1, i2}
		}
	}
	return []int{i1, i2}
}

func binarySearch(numbers []int, target int, start int) int {
	if len(numbers) == 0 {
		return -1
	}

	mid := len(numbers) / 2

	if numbers[mid] == target {
		return mid + start
	}
	if numbers[mid] > target {
		return binarySearch(numbers[:mid], target, start)
	}
	return binarySearch(numbers[mid+1:], target, start+mid+1)
}
