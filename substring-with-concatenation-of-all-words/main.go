package main

func findSubstring(s string, words []string) []int {
	n := len(words[0])
	count := len(words)
	memory := make(map[string]int)
	result := []int{}
	for _, word := range words {
		memory[word] += 1
	}

	for i := 0; i < n; i++ {
		exec(s, n, count, i, &memory, &result)
	}

	return result
}

func exec(s string, n int, count int, pos int, memory *map[string]int, result *[]int) {
	counter := 0

	left := pos
	right := left + n

	for right <= len(s) {
		w := s[right-n : right]
		c, prs := (*memory)[w]
		if !prs {
			for left < right {
				v := s[left : left+n]
				if _, prs := (*memory)[v]; prs {
					(*memory)[v] += 1
				}
				left += n
			}
			right = left + n
			counter = 0
		} else if c == 0 {
			for (*memory)[w] == 0 {
				v := s[left : left+n]
				(*memory)[v] += 1
				left += n
				counter -= 1
			}
		} else {
			counter += 1
			(*memory)[w] -= 1
			right += n
		}

		if counter == count {
			(*result) = append((*result), left)
			v := s[left : left+n]
			(*memory)[v] += 1
			counter -= 1
			left += n
		}
	}

	for left+n <= len(s) {
		v := s[left : left+n]
		if _, prs := (*memory)[v]; prs {
			(*memory)[v] += 1
		}
		left += n
	}
}
