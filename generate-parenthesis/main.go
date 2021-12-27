package main

import (
	"fmt"
	"strings"
)

// func generateParenthesis(n int) []string {
//     if n == 0 {
//         return []string{""}
//     }

//     ans := []string{}

//     for c:=0; c<n; c++ {
//         for _, left := range generateParenthesis(c) {
//             for _, right := range generateParenthesis(n-1-c) {
//                 ans = append(ans, fmt.Sprintf("(%s)%s", left, right))
//             }
//         }
//     }

//     return ans
// }

func generateParenthesis(n int) []string {
	ans := []string{}

	backTrack(&ans, &[]string{}, n, 0, 0)

	return ans
}

func backTrack(ans *[]string, s *[]string, n int, left int, right int) {
	if len(*s) == 2*n {
		*ans = append(*ans, strings.Join((*s)[:], ""))
		return
	}

	if left < n {
		*s = append(*s, "(")
		backTrack(ans, s, n, left+1, right)
		*s = (*s)[:len(*s)-1]
	}

	if right < left {
		*s = append(*s, ")")
		backTrack(ans, s, n, left, right+1)
		*s = (*s)[:len(*s)-1]
	}

	return
}

func main() {
	fmt.Println(generateParenthesis(3))
}
