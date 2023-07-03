package main

func buddyStrings(s string, goal string) bool {
	if len(s) != len(goal) {
		return false
	}
	swaps := make([]int, 2)
	swaps[0], swaps[1] = -1, -1

	for i := 0; i < len(s); i++ {
		if s[i] != goal[i] {
			if swaps[0] == -1 {
				swaps[0] = i
			} else if swaps[1] == -1 {
				swaps[1] = i
			} else {
				return false
			}
		}
	}

	if swaps[0] == -1 && swaps[1] == -1 {
		m := make(map[rune]int)
		for i := 0; i < len(s); i++ {
			if v := m[rune(s[i])]; v >= 1 {
				return true
			}
			m[rune(s[i])]++
		}
	} else if swaps[0] >= 0 && swaps[1] >= 0 {
		if s[swaps[0]] == goal[swaps[1]] && s[swaps[1]] == goal[swaps[0]] {
			return true
		}
	}
	return false
}
