package main

/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guess(num int) int

func guessNumber(n int) int {
	min, max := 1, n

	m := (min + max) / 2
	for min < max {
		switch v := guess(m); v {
		case -1:
			max = m - 1
		case 1:
			min = m + 1
		default:
			return m
		}
		m = (min + max) / 2
	}

	return min
}
