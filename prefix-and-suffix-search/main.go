package main

type WordFilter struct {
	prefix map[string][]int
	suffix map[string][]int
}

func Constructor(words []string) WordFilter {
	wf := WordFilter{make(map[string][]int), make(map[string][]int)}

	for i, word := range words {
		for j := 0; j < len(word); j++ {
			if _, ok := wf.prefix[word[:j+1]]; ok {
				wf.prefix[word[:j+1]] = append(wf.prefix[word[:j+1]], i)
			} else {
				wf.prefix[word[:j+1]] = []int{i}
			}
			if _, ok := wf.suffix[word[len(word)-1-j:]]; ok {
				wf.suffix[word[len(word)-1-j:]] = append(wf.suffix[word[len(word)-1-j:]], i)
			} else {
				wf.suffix[word[len(word)-1-j:]] = []int{i}
			}
		}
	}

	// fmt.Println(wf.prefix)
	// fmt.Println(wf.suffix)

	return wf
}

func (this *WordFilter) F(prefix string, suffix string) int {
	if pref, ok := this.prefix[prefix]; ok {
		if suff, ok := this.suffix[suffix]; ok {
			for i := 0; i < len(pref); i++ {
				r := search(pref[len(pref)-1-i], suff)
				if r != -1 {
					return r
				}
			}
		}
	}
	return -1
}

func search(num int, nums []int) int {
	n := len(nums)
	if n == 0 {
		return -1
	}
	m := n / 2

	if nums[m] == num {
		return num
	} else if nums[m] < num {
		return search(num, nums[m+1:])
	}
	return search(num, nums[:m])
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * obj := Constructor(words);
 * param_1 := obj.F(prefix,suffix);
 */
