package number

func hammingWeight(num uint32) int {
	result := 0
	for num > 0 {
		temp := num & 1
		if temp == 1 {
			result++
		}
		num = num >> 1
	}
	return result
}
