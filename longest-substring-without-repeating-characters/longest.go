package longest

func lengthOfLongestSubstring(s string) int {
	mLen, cLen, sIdx := 0, 0, 0

	magic := map[rune]int{}

	for idx, val := range s {
		if lIdx, ok := magic[val]; ok && lIdx >= sIdx {
			sIdx = lIdx + 1
			cLen = idx - lIdx
		} else {
			cLen++
		}

		if cLen > mLen {
			mLen = cLen
		}

		magic[val] = idx
	}

	return mLen
}
