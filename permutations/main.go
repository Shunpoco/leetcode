package main

type T struct {
	vals  []int
	level int
}

func permute(nums []int) [][]int {
	L := len(nums)
	stack := []T{{vals: []int{}, level: 0}}
	result := [][]int{}

	for len(stack) > 0 {
		t := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		vals := t.vals
		level := t.level

		for _, num := range nums {
			if !isin(vals, num) {
				var temp = make([]int, len(vals), len(vals)+1)
				copy(temp, vals)
				temp = append(temp, num)
				if len(temp) == L {
					result = append(result, temp)
				} else {
					stack = append(stack, T{vals: temp, level: level + 1})
				}
			}
		}
	}

	return result
}

func isin(vals []int, target int) bool {
	for _, val := range vals {
		if val == target {
			return true
		}
	}
	return false
}
