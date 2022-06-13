package main

func rangeBitwiseAnd(left int, right int) int {
	result := 0

	for left > 0 && right > 0 {
		b := 1
		for b <= left {
			b *= 2
		}
		if b > left {
			b /= 2
		}
		if b*2 <= right {
			break
		}
		result += b
		left -= b
		right -= b
	}

	return result
}
