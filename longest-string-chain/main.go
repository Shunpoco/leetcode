package main

import "sort"

func longestStrChain(words []string) int {
	sort.Slice(words, func(i, j int) bool { return len(words[i]) < len(words[j]) })

	memory := make(map[int]int)
	result := chain(-1, &words, &memory)

	return result
}

func chain(idx int, words *[]string, memory *map[int]int) int {
	if v, ok := (*memory)[idx+1]; ok {
		return v
	}

	var result int
	for next := idx + 1; next < len(*words); next++ {
		if idx == -1 || isPredecessor((*words)[idx], (*words)[next]) {
			t := 1 + chain(next, words, memory)
			if result < t {
				result = t
			}
		}
	}

	(*memory)[idx+1] = result

	return result
}

func isPredecessor(word1, word2 string) bool {
	l1 := len(word1)
	l2 := len(word2)
	if l1+1 != l2 {
		return false
	}

	idx1 := 0
	for idx2 := 0; idx2 < l2; idx2++ {
		if idx1 < l1 && word1[idx1] == word2[idx2] {
			idx1++
		}
	}

	if idx1 != l1 {
		return false
	}
	return true
}
