package main

import "sort"

func maxArea(h int, w int, hc []int, vc []int) int {
	sort.Slice(hc, func(i, j int) bool { return hc[i] < hc[j] })
	sort.Slice(vc, func(i, j int) bool { return vc[i] < vc[j] })

	mh := hc[0]
	mv := vc[0]
	for i := 1; i < len(hc)+1; i++ {
		var v int
		if i == len(hc) {
			v = h - hc[i-1]
		} else {
			v = hc[i] - hc[i-1]
		}
		if v > mh {
			mh = v
		}
	}

	for i := 1; i < len(vc)+1; i++ {
		var v int
		if i == len(vc) {
			v = w - vc[i-1]
		} else {
			v = vc[i] - vc[i-1]
		}
		if v > mv {
			mv = v
		}
	}

	return mh * mv % 1000000007
}
