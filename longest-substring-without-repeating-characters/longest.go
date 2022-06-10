package longest

func lengthOfLongestSubstring(s string) int {
	memory := make(map[rune]int)
	left := 0
	result := 0

	for right := 0; right < len(s); right++ {
		r := rune(s[right])
		if v, ok := memory[r]; ok && v >= left {
			left = v + 1
		}
		memory[r] = right

		if right-left+1 > result {
			result = right - left + 1
		}
	}

	return result
}
