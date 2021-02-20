package majority

func majorityElement(nums []int) int {
	hash := map[int]int{}

	for _, val := range nums {
		hash[val]++
	}

	half := len(nums) / 2
	majorityVal := 0
	majorityCount := 0
	for val, count := range hash {
		if count > majorityCount {
			majorityVal = val
			majorityCount = count
		}

		if majorityCount > half {
			return majorityVal
		}
	}

	return majorityVal
}
