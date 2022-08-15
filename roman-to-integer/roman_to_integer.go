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
			i++
		}
		result = result + temp
		i++
	}

	return result
}

// 2022/08/15 use stack
// func romanToInt(s string) int {
// 	stack := []rune{}
// 	var result int
// 	for _, c := range s {
// 		switch c {
// 		case 'M':
// 			if len(stack) > 0 && stack[len(stack)-1] == 'C' {
// 				result += 900
// 				stack = stack[:len(stack)-1]
// 			} else {
// 				result += 1000
// 			}
// 		case 'D':
// 			if len(stack) > 0 && stack[len(stack)-1] == 'C' {
// 				result += 400
// 				stack = stack[:len(stack)-1]
// 			} else {
// 				result += 500
// 			}
// 		case 'C':
// 			if len(stack) > 0 && stack[len(stack)-1] == 'X' {
// 				result += 90
// 				stack = stack[:len(stack)-1]
// 			} else {
// 				stack = append(stack, c)
// 			}
// 		case 'L':
// 			if len(stack) > 0 && stack[len(stack)-1] == 'X' {
// 				result += 40
// 				stack = stack[:len(stack)-1]
// 			} else {
// 				result += 50
// 			}
// 		case 'X':
// 			if len(stack) > 0 && stack[len(stack)-1] == 'I' {
// 				result += 9
// 				stack = stack[:len(stack)-1]
// 			} else {
// 				stack = append(stack, c)
// 			}
// 		case 'V':
// 			if len(stack) > 0 && stack[len(stack)-1] == 'I' {
// 				result += 4
// 				stack = stack[:len(stack)-1]
// 			} else {
// 				result += 5
// 			}
// 		default:
// 			stack = append(stack, c)
// 		}
// 	}

// 	for len(stack) > 0 {
// 		switch c := stack[len(stack)-1]; c {
// 		case 'M':
// 			result += 1000
// 		case 'D':
// 			result += 500
// 		case 'C':
// 			result += 100
// 		case 'L':
// 			result += 50
// 		case 'X':
// 			result += 10
// 		case 'V':
// 			result += 5
// 		default:
// 			result += 1
// 		}
// 		stack = stack[:len(stack)-1]
// 	}

// 	return result
// }
