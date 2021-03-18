package twosum

func twoSum(nums []int, target int) []int {
	hash := map[int]int{}

	for idx, val := range nums {
		hash[target-val] = idx + 1
	}

	for idx, val := range nums {
		if hash[val] != 0 && idx+1 != hash[val] {
			return []int{idx, hash[val] - 1}
		}
	}
	return []int{}
}
