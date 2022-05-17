package main

import (
	"fmt"
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

// func generateParenthesis(n int) []string {
// 	ans := []string{}

// 	backTrack(&ans, &[]string{}, n, 0, 0)

// 	return ans
// }

// func backTrack(ans *[]string, s *[]string, n int, left int, right int) {
// 	if len(*s) == 2*n {
// 		*ans = append(*ans, strings.Join((*s)[:], ""))
// 		return
// 	}

// 	if left < n {
// 		*s = append(*s, "(")
// 		backTrack(ans, s, n, left+1, right)
// 		*s = (*s)[:len(*s)-1]
// 	}

// 	if right < left {
// 		*s = append(*s, ")")
// 		backTrack(ans, s, n, left, right+1)
// 		*s = (*s)[:len(*s)-1]
// 	}

// 	return
// }

func generateParenthesis(n int) []string {
	memory := make(map[int][]string)
	memory[0] = []string{""}
	memory[1] = []string{"()"}
	result := parenthesis(n, &memory)
	// fmt.Println(memory)

	return result
}

func parenthesis(n int, memory *map[int][]string) []string {
	if v, prs := (*memory)[n]; prs {
		return v
	}

	result := []string{}
	m := make(map[string]bool)

	for i := 0; i < n; i++ {
		for j := 0; j < n-i; j++ {
			k := (n - 1) - i - j
			ci := parenthesis(i, memory)
			cj := parenthesis(j, memory)
			ck := parenthesis(k, memory)

			for _, vi := range ci {
				for _, vj := range cj {
					for _, vk := range ck {
						v := fmt.Sprintf("%s(%s)%s", vi, vj, vk)
						if _, prs := m[v]; !prs {
							result = append(result, v)
							m[v] = true
						}
					}
				}
			}
		}
	}

	(*memory)[n] = result

	return result
}

func main() {
	fmt.Println(generateParenthesis(3))
}
