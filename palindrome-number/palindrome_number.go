package palindromeNumber

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}

	temp := []int{}
	for i := 0; x > 0; i++ {
		temp = append(temp, x%10)
		x = x / 10
	}

	for i := 0; i < len(temp); i++ {
		if temp[i] != temp[len(temp)-1-i] {
			return false
		}
	}
	return true
}
