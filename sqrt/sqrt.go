package mySqrt

// we can user binary search
// see https://leetcode.com/problems/sqrtx/discuss/1031472/Binary-search-solution-wvideo-whiteboard-explanation
func mySqrt(x int) int {
	l, r := 0, x

	for l <= r {
		mid := (l + r) / 2
		midSq := mid * mid

		if midSq > x {
			r = mid - 1
		} else if midSq < x {
			l = mid + 1
		} else {
			return mid
		}
	}

	return l - 1
}
