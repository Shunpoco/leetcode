package main

import "sort"

func maxArea(h int, w int, hc []int, vc []int) int {
	sort.Slice(hc, func(i, j int) bool { return hc[i] < hc[j] })
	sort.Slice(vc, func(i, j int) bool { return vc[i] < vc[j] })

	mh := 0
	mv := 0
	for i, num := range hc {
		var v int
		if i == 0 {
			v = num
		} else {
			v = num - hc[i-1]
		}
		if v > mh {
			mh = v
		}
	}
	if h-hc[len(hc)-1] > mh {
		mh = h - hc[len(hc)-1]
	}

	for i, num := range vc {
		var v int
		if i == 0 {
			v = num
		} else {
			v = num - vc[i-1]
		}
		if v > mv {
			mv = v
		}
	}
	if w-vc[len(vc)-1] > mv {
		mv = w - vc[len(vc)-1]
	}

	return mh * mv % 1000000007
}
