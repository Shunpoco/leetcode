package main

type Sub struct {
	Len  int
	Last int
}

func isPossible(nums []int) bool {
	subs := []Sub{Sub{1, nums[0]}}

	for _, num := range nums[1:] {
		l := 100000
		idx := -1
		for i, sub := range subs {
			if sub.Last+1 == num && sub.Len < l {
				l = sub.Len
				idx = i
			}
		}

		if idx == -1 {
			subs = append(subs, Sub{1, num})
		} else {
			subs[idx].Last = num
			subs[idx].Len++
		}
	}

	for _, sub := range subs {
		if sub.Len < 3 {
			return false
		}
	}

	return true
}
