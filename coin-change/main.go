package main

func coinChange(coins []int, amount int) int {
	memory := make(map[int]int)

	result := dp(amount, &coins, &memory)

	return result
}

func dp(amount int, coins *[]int, memory *map[int]int) int {
	if m, prs := (*memory)[amount]; prs {
		return m
	}

	if amount == 0 {
		return 0
	} else if amount < 0 {
		return -1
	}

	result := -1
	for _, v := range *coins {
		t := dp(amount-v, coins, memory)
		if t != -1 && (result == -1 || result > t+1) {
			result = t + 1
		}
	}

	(*memory)[amount] = result

	return result
}
