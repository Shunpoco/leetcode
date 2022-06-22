package main

type Heap []int

func (h Heap) Len() int {
	return len(h)
}

func (h *Heap) Swap(i, j int) {
	(*h)[i], (*h)[j] = (*h)[j], (*h)[i]
}

func (h *Heap) Pop() int {
	n := (*h).Len()
	result := (*h)[0]
	(*h)[0] = (*h)[n-1]
	*h = (*h)[:n-1]
	if n == 1 {
		return result
	}

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

func kthSmallest(matrix [][]int, k int) int {
	n := len(matrix)
	heap := Heap{}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			heap.Push(matrix[i][j])
		}
	}

	var result int
	for i := 0; i < k; i++ {
		result = heap.Pop()
	}

	return result
}
