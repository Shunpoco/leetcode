package main

func reorderedPowerOf2(n int) bool {
	digits := 0
	t := n
	for t > 0 {
		digits++
		t /= 10
	}

	lower := 0
	upper := 0
	for i := 0; i < digits; i++ {
		if i == 0 {
			lower = 1
			upper = 9
		} else {
			lower *= 10
			upper = upper*10 + 9
		}
	}

	candidates := []int{}
	start := 1
	for start <= upper {
		if start >= lower {
			candidates = append(candidates, start)
		}
		start *= 2
	}

	for _, candidate := range candidates {
		if check(candidate, n) {
			return true
		}
	}

	return false
}

func check(candidate, n int) bool {
	memory := make(map[int]int)
	for n > 0 {
		memory[n%10]++
		n /= 10
	}

	for candidate > 0 {
		v := candidate % 10
		if memory[v] <= 0 {
			return false
		}
		memory[v]--
		candidate /= 10
	}

	return true
}
