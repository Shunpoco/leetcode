package twoSum

func twoSum(nums []int, target int) []int {
	// define hashtable: key is number in array, value is index + 1 of array.
	hashtable := map[int][]int{}

	for idx, val := range nums {
		hashtable[val] = append(hashtable[val], idx+1)
	}
	var i, j int
	for val, idx := range hashtable {
		sub := target - val
		if val == sub && len(idx) > 1 {
			i = idx[0] - 1
			j = idx[1] - 1
			break
		} else if val != sub && len(hashtable[sub]) != 0 {
			i = idx[0] - 1
			j = hashtable[target-val][0] - 1
			break
		}
	}
	if i > j {
		i, j = j, i
	}
	return []int{i, j}
}

// 2021-08-20
func twoSum(nums []int, target int) []int {
	h := make(map[int]int)

	for i, v := range nums {
		j, ok := h[v]
		if ok {
			return []int{j, i}
		}
		h[target-v] = i
	}

	return []int{0}
}
