package main

func findSubstring(s string, words []string) []int {
	n := len(words[0])
	memory := make(map[string]int)
	for _, word := range words {
		memory[word] += 1
	}
	count := len(words)
	result := []int{}

	for i := 0; i < len(s)-n+1; i++ {
		if bt(s, n, i, i, count, &memory) {
			result = append(result, i)
		}
	}

	return result
}

func bt(s string, n int, base int, cur int, count int, memory *map[string]int) bool {
	if count == 0 {
		return true
	}

	if cur+n > len(s) {
		return false
	}

	v := s[cur : cur+n]
	if (*memory)[v] == 0 {
		return false
	}

	var result bool

	(*memory)[v] -= 1
	count -= 1
	result = bt(s, n, base, cur+n, count, memory)
	count += 1
	(*memory)[v] += 1

	return result
}
