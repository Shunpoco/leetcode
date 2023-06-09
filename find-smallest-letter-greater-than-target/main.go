package main

func nextGreatestLetter(letters []byte, target byte) byte {
	return letters[bs(letters, target, 0, len(letters))]
}

func bs(letters []byte, target byte, left, right int) int {
	if left == right {
		if left == len(letters) {
			return 0
		}
		return left
	}

	m := (left + right) / 2

	if letters[m] <= target {
		return bs(letters, target, m+1, right)
	} else {
		return bs(letters, target, left, m)
	}
}
