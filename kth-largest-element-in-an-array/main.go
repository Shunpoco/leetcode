package main

type Heap []int

func (h Heap) Len() int {
	return len(h)
}

func (h *Heap) Push(num int) {
	n := (*h).Len()
	*h = append(*h, num)
	var p int
	if n%2 == 0 {
		p = (n - 2) / 2
	} else {
		p = (n - 1) / 2
	}
	for p >= 0 && (*h)[p] > (*h)[n] {
		h.Swap(p, n)
		n = p
		if n%2 == 0 {
			p = (n - 2) / 2
		} else {
			p = (n - 1) / 2
		}
	}
}

func (h *Heap) Swap(i, j int) {
	(*h)[i], (*h)[j] = (*h)[j], (*h)[i]
}

func (h *Heap) Pop() int {
	n := (*h).Len()
	result := (*h)[0]
	(*h)[0] = (*h)[n-1]
	if n == 1 {
		return result
	}
	(*h) = (*h)[:n-1]
	base := 0
	idx := base
	left := 2*base + 1
	right := 2*base + 2
	v := (*h)[base]
	for left < n-1 {
		if v > (*h)[left] {
			v = (*h)[left]
			idx = left
		}
		if right < n-1 && v > (*h)[right] {
			v = (*h)[right]
			idx = right
		}
		if base != idx {
			h.Swap(base, idx)
			base = idx
			idx = base
			left = 2*base + 1
			right = 2*base + 2
			v = (*h)[base]
		} else {
			break
		}
	}

	return result
}

func findKthLargest(nums []int, k int) int {
	hp := Heap{}
	for _, num := range nums {
		hp.Push(-num)
	}

	count := 0
	v := 0
	for count < k {
		v = hp.Pop()
		count++
	}

	return -v
}
