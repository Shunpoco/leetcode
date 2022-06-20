package main

func minimumLengthEncoding(words []string) int {
    result := []string{words[0]}
    
    for i := 1; i < len(words); i++ {
        v := words[i]
        lv := len(v)
        cont := false
        for j := 0; j < len(result); j++ {
            c := result[j]
            lc := len(c)
            
            if lv > lc {
                if isSubstring(v, c) {
                    result[j] = v
                    cont = true
                    break
                }
            } else {
                if isSubstring(c, v) {
                    cont = true
                    break
                }
            }
        }
        if !cont {
            result = append(result, v)
        }
    }
    
    r := 0
    for _, v := range result {
        r += len(v) + 1
    }
    
    return r
}

func isSubstring(word1, word2 string) bool {
    // len(word1) >= len(word2)
    for i := 0; i < len(word2); i++ {
        if word1[len(word1)-1-i] != word2[len(word2)-1-i] {
            return false
        }
    }
    
    return true
}
