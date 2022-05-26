package number

func hammingWeight(num uint32) int {
	result := 0
	for num > 0 {
		if num&1 == 1 { // also num%2 == 1
			result++
		}
		num >>= 1
	}

	return result
}
