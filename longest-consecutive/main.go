package main

func longestConsecutive(nums []int) int {
	memory := make(map[int]bool)
	for _, num := range nums {
		memory[num] = true
	}

	var result int
	for k, _ := range memory {
		if _, ok := memory[k-1]; !ok {
			cur := k
			t := 1
			for {
				if _, ok = memory[cur+1]; ok {
					cur++
					t++
				} else {
					break
				}
			}

			if t > result {
				result = t
			}
		}
	}

	return result
}
