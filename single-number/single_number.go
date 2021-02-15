package singleNumber

func singleNumber(nums []int) int {
	hash := map[int]int{}

	for _, val := range nums {
		hash[val] = hash[val] + 1
	}

	for _, val := range nums {
		if hash[val] == 1 {
			return val
		}
	}

	return 0
}

func singleNumber2(nums []int) int {
	res := 0

	for _, val := range nums {
		res = res ^ val
	}

	return res
}
