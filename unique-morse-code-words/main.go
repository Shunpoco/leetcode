package main

func uniqueMorseRepresentations(words []string) int {
	table := []string{".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."}
	memo := make(map[string]bool)

	for _, word := range words {
		t := ""
		for _, c := range word {
			t += table[c-'a']
		}

		memo[t] = true
	}

	return len(memo)
}
