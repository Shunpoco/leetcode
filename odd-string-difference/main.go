package main

func oddString(words []string) string {
	m := len(words)
	n := len(words[0])

	for j := 0; j < n-1; j++ {
		mem := make(map[int][]int)
		for i := 0; i < m; i++ {
			mem[int(words[i][j+1])-int(words[i][j])] = append(mem[int(words[i][j+1])-int(words[i][j])], i)
		}

		if len(mem) > 1 {
			for _, value := range mem {
				if len(value) == 1 {
					return words[value[0]]
				}
			}
		}
	}

	return ""
}
