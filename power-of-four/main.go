package main

func isPowerOfFour(n int) bool {
	if n&(n-1) == 0 && n%3 == 1 {
		return true
	}

	return false
}
