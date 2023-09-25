package main

func main() {

    findTheDifference("abcd", "abcde")
}

func findTheDifference(s string, t string) byte {
        memo := make(map[rune]int)

        for _, c := range s {
            memo[c]++
        }

        for _, c := range t {
            memo[c]--

            if memo[c] < 0 {
                return byte(c)
            }
        }

        return t[0]
}

