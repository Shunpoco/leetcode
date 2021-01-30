package validParentheses

func isValid(s string) bool {
	matcher := map[rune]rune{
		'(': ')',
		'{': '}',
		'[': ']',
	}
	stackOpen := make([]rune, 0)

	for _, val := range s {
		if val == '(' || val == '{' || val == '[' {
			stackOpen = append(stackOpen, val)
		} else {
			if len(stackOpen) == 0 {
				return false
			}
			poped := stackOpen[len(stackOpen)-1]
			stackOpen = stackOpen[:len(stackOpen)-1]
			if matcher[poped] != val {
				return false
			}
		}
	}
	if len(stackOpen) != 0 {
		return false
	}
	return true
}
