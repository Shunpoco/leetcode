package main

func firstUniqChar(s string) int {
	char_count := make([]int, 26)
	char_position := make([]int, 26)

	for i, c := range s {
		char_count[c-'a']++
		if char_count[c-'a'] == 1 {
			char_position[c-'a'] = i
		}
	}

	result := -1
	for i := 0; i < 26; i++ {
		if char_count[i] == 1 && (result == -1 || char_position[i] < result) {
			result = char_position[i]
		}
	}

	return result
}
