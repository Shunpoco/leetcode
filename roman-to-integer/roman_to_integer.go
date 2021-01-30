package romanToInt

func romanToInt(s string) int {
	matcher := map[rune]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	var result int

	for i := 0; i < len(s); {
		temp := matcher[rune(s[i])]
		if i < len(s)-1 && temp < matcher[rune(s[i+1])] {
			temp = matcher[rune(s[i+1])] - temp
			i = i + 1
		}
		result = result + temp
		i = i + 1
	}

	return result
}
