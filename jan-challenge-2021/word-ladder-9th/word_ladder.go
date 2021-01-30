// time exceeded...
// use BFS to solve the problem
package wordLadder

func ladderLength(beginWord string, endWord string, wordList []string) int {
	result := subProcess(beginWord, endWord, wordList, 1)
	if result == 999 {
		return 0
	}
	return result
}

func subProcess(bWord string, eWord string, wList []string, length int) int {
	length = length + 1
	match := []string{}
	nomatch := []string{}

	for _, val := range wList {
		if isMatch(bWord, val) {
			if val == eWord {
				return length
			}
			match = append(match, val)
		} else {
			nomatch = append(nomatch, val)
		}
	}
	result := 999

	if len(match) == 0 || len(nomatch) == 0 {
		return 999
	}

	for _, val := range match {
		temp := subProcess(val, eWord, nomatch, length)
		if result > temp {
			result = temp
		}
	}
	return result
}

func isMatch(w1, w2 string) bool {
	count := 0
	for i := 0; i < len(w1); i++ {
		if w1[i] != w2[i] {
			count = count + 1
		}
	}
	if count == 1 {
		return true
	}
	return false
}
