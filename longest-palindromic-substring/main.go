package main

func longestPalindrome(s string) string {
	n := len(s)

	if n == 0 {
		return ""
	}

	start, end := 0, 0

	for i := 0; i < n; i++ {
		l1 := window(s, i, i)
		l2 := window(s, i, i+1)
		l := l1
		if l2 > l {
			l = l2
		}

		if l > end-start+1 {
			start = i - (l-1)/2 // l1を採用した場合、 l/2 == (l-1)/2, l2を採用した場合、iが真ん中2つの左の項なので調整が必要
			end = i + l/2
		}
	}

	return s[start : end+1]
}

func window(s string, l, r int) int {
	for l >= 0 && r < len(s) && s[l] == s[r] {
		l--
		r++
	}

	return r - l - 1
}
