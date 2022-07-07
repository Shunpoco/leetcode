package main

func generateParenthesis(n int) []string {
	result := []string{}
	solve(n, n, "", &result)

	return result
}

func solve(left, right int, s string, result *[]string) {
	if left == 0 && right == 0 {
		*result = append(*result, s)
		return
	}

	if left > 0 {
		solve(left-1, right, s+"(", result)
	}

	if left < right {
		solve(left, right-1, s+")", result)
	}
}
