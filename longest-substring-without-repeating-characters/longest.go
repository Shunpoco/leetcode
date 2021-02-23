package longest

func lengthOfLongestSubstring(s string) int {
	result := 0

	temp := 0

	l := len(s)

	for i := 0; i < l; i++ {
		hash := map[string]int{}
		word := string(s[i])
		temp = 1
		hash[word]++
		for j := i + 1; j < l; j++ {
			word := string(s[j])
			hash[word]++
			if hash[word] == 1 {
				temp++
			}
			if hash[word] > 1 {
				break
			}
		}
		if temp > result {
			result = temp
		}
	}
	return result
}
