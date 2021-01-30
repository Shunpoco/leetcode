package reverse

const MAX = 2147483647
const MIN = -2147483648

func reverseInteger(x int32) int32 {
	var output int64
	var digit int32 = 1

	if x < 0 {
		digit = -1
		x = x * -1
	}

	for x > 0 {
		output = output*10 + int64(x%10)
		x = x / 10
	}

	if output > MAX || output < MIN {
		output = 0
	}

	return int32(output) * digit
}
