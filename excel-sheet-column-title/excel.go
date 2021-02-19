package excel

var MATCHER = map[int]rune{
	1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
	6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
	11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
	16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
	21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
	26: 'Z',
}

func convertToTitle(n int) string {
	if n <= 0 {
		return ""
	}
	v := twentySix(n)
	r := ""
	for i := len(v) - 1; i >= 0; i-- {
		r += string(MATCHER[v[i]])
	}
	return r
}

func twentySix(n int) []int {
	r := []int{}
	for n > 0 {
		v := n % 26
		if v == 0 {
			v = 26
		}
		r = append(r, v)
		n = (n - v) / 26
	}
	return r
}
