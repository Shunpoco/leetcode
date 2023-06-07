package main

func minFlips(a int, b int, c int) int {
	sab := make([]int, 64)

	for i := 0; a > 0; i++ {
		sab[i] += a & 1
		a >>= 1
	}

	for i := 0; b > 0; i++ {
		sab[i] += b & 1
		b >>= 1
	}

	var result int

	for i := 0; i < 64; i++ {
		v := 0
		if c > 0 {
			v = c & 1
			c >>= 1
		}

		switch sab[i] {
		case 2:
			if v == 0 {
				result += 2
			}
		case 1:
			if v == 0 {
				result += 1
			}
		default:
			if v == 1 {
				result += 1
			}
		}
	}

	return result
}
