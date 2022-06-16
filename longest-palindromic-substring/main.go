package main

func longestPalindrome(s string) string {
	n := len(s)

	if n == 0 {
		return ""
	}

	start := 0
	end := 0

	for i := 0; i < n; i++ {
		l1 := window(s, i, i)
		l2 := window(s, i, i+1)

		l := l1
		if l < l2 {
			l = l2
		}

		if l > end-start {
			start = i - (l-1)/2
			end = i + l/2
		}
	}

	return s[start : end+1]
}

func window(s string, left, right int) int {
	l := left
	r := right

	for l >= 0 && r < len(s) && s[l] == s[r] {
		l--
		r++
	}

	return r - l - 1
}
